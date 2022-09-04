# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 22:59:45 2022

@author: danny
"""

import pygame
import solve

import time

import find_moves.update_moves as find
import find_moves.valid_move as valid_moves

import graphics.get_click_pos as click

Game = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Game Test")

pygame.init()

font = pygame.font.SysFont("comicsans", 45)

clock = pygame.time.Clock()

# Colours
white = (255, 255, 255)
black = (0, 0, 0)
lime = (0, 255, 0)
blue = (0, 0, 255)
red = (128, 0, 0)
navy = (128,0,128)
    
class square ():
    
    def __init__(self, value, row, col, width, total_rows):
        
        self.value = value
        self.row = row
        self.col = col      
        self.x = row * width
        self.y = col * width
        self.width = width
        
        self.st = False
        
        self.colour = (255, 255, 255)
        
        self.previous_value = -99;
        
        self.neighbours = []
        self.possible_moves = []
        
        self.total_rows = total_rows
        
        self.visited = False
        self.root = None
        self.next = None
        
        self.text_surf = font.render(f"{self.value}",True, black)
        
    def get_pos(self):
        
        return (self.row, self.col)
    
    def set_next(self, value):
        
        self.next = value
    
    def set_visited(self, yes):
        self.visited = yes
    
    def set_value(self, value):
        
        self.value = value
        
    def set_root(self, value):
        
        self.root = value
        
    def get_value(self):
        
        return self.value
    
    def set_previous_value(self, previous_value):
        
        self.previous_value = previous_value
        
    def get_clicked(self, grid, start):
        
        #print(update_moves(grid, self.row, self.col))
        
        if (self.value < 9):
            
            index = 0
            
            while True:
                
                if (start):
                    self.st = True
                
                if (len(self.neighbours) > 0):
                    
                    self.value += 1
                    index += 1
                    
                    if (self.value > 9):
                        
                        self.value = 1
                    
                    if (index == 10):
                        return False
                    
                    if valid_moves.is_valid_num(grid, self.row, self.col, self.value):
                        
                        break
                    else:
    
                        continue
                    
                else:
                    
                    break
                    
        else:
            
            self.value = 0
            
            self.st = False
            
        if (self.value > 9):
            
            self.value = 0
            
            self.st = False
        
        self.text_surf = font.render(f"{self.value}",True, black)
        
    def delete_click(self, grid):
        
        if (self.value > 0):
            
            while True:
                    
                    self.value -= 1
                    
                    if valid_moves.is_valid_num(grid, self.row, self.col, self.value) or self.value < 1:
                        break
                        self.st = False
                    else:
                        continue
            
        self.text_surf = font.render(f"{self.value}",True, black) 
    
    # Draw square
    def draw(self, Game):
        
        pygame.draw.rect(Game, self.colour, (self.x, self.y, self.width, self.width))
        
        self.text_surf = font.render(f"{self.value}",True, black)
        
        Game.blit(self.text_surf, (self.x + 35, self.y + 25))
    
    # Place all valid neighbours into neighbours list
    def find_nearby_spots(self, matrix):
        
        self.neighbours = find.update_moves(matrix, self.row, self.col)
        
            
    # Less than operator
    def __lt__ (self, other):
        return False
            
def draw(Game, grid, rows, width):
    
    Game.fill(white)

    for x in grid:
        
        for square in x:
            
            square.draw(Game)


    draw_grid(Game, rows, width)
    
    pygame.display.update()
    
def make_grid(rows, width):
    
    grid = []
    
    for x in range(rows):
        
        temp = []
        
        for y in range(rows):
            
            # Create square objects
            spot = square(0, x, y, (width // rows), rows)
            
            temp.append(spot)
            
        grid.append(temp)

    return grid

# draw grid
def draw_grid(Game, rows, width):
    
    # Gap for each square
    gap = width // rows
    
    for i in range(rows+1):
        
        # Draw lines (horizontal)
        if (i % 3 == 0):
            
            pygame.draw.line(Game, black, (0, i * gap), (width, i * gap), 5)
            
        else:
            
            pygame.draw.line(Game, black, (0, i * gap), (width, i * gap), 1)
        
        for j in range(rows+1):
            
            # Draw lines (vertical)
            
            if (j % 3 == 0):
                
                pygame.draw.line(Game, black, (j * gap, 0), (j * gap, width), 5)
                
            else:
                
                pygame.draw.line(Game, black, (j * gap, 0), (j * gap, width), 1)
            
def main(Game, rows, width):
    
    grid = make_grid(rows, width)
    
    run = True
    
    while (run):
        
        clock.tick(30)
    
        draw(Game, grid, rows, width)
        
        for event in pygame.event.get():
            
            # Quit game
            if event.type == pygame.QUIT:
                
                run = False
            
            if pygame.mouse.get_pressed()[0]:
            
                pos = pygame.mouse.get_pos()
                
                row, col = click.get_clicked_pos(pos, rows, width)
                
                if (row < rows):
                
                    spot = grid[row][col]
                                    
                    #spot.find_nearby_spots(grid)
                    
                    spot.find_nearby_spots(grid)
                    
                    spot.get_clicked(grid, True)
                    
            if pygame.mouse.get_pressed()[2]:
            
                pos = pygame.mouse.get_pos()
                
                row, col = click.get_clicked_pos(pos, rows, width)
                
                if (row < rows):
                
                    spot = grid[row][col]
                                    
                    #spot.find_nearby_spots(grid)
                    
                    spot.find_nearby_spots(grid)
                    
                    spot.delete_click(grid)
                    
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_SPACE:
                
                    start_time = time.time()
                    
                    solve.solve_sudoku(grid, (lambda: draw(Game, grid, rows, width)))
                    
                    print("--- %s seconds ---" % (time.time() - start_time))
                    
                elif event.key == pygame.K_c:
                    
                    grid = make_g.make_grid(rows, width)
                    
    
main(Game, 9, 801)