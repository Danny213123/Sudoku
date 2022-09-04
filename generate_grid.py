# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 22:59:45 2022

@author: danny
"""

import pygame
import solve

import time

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

def find_neighbours(i, j):
    
    # LEFT  x,   y-1
    # RIGHT x,   y+1
    # UP    x+1, y
    # DOWN  x-1, y
    
    #return [(i+1,j), (i-1,j), (i,j+1), (i,j-1), (i+1,j+1), (i-1,j-1), (i-1,j+1), (i+1,j-1)]
    return [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]

# Check if neighbour x_pos and y_pos within boundaries
def is_valid(i, j, m_row):
    
    if (0 <= i < m_row and 0 <= j < m_row):
                
        return True
    
    else:
        
        return False
    
def update_moves (grid, row, col):
    
    moves = []
    
    for x in range(1, 10):
        
        if (is_valid_num(grid, row, col, x)):
            
            moves.append(x)
            
    return moves
    
def is_valid_num (grid, row, col, number):
    
    #print(number)
    
    if (0 <= row < 3 and 0 <= col < 3):
        
        min_x, min_y, max_x, max_y = 0, 0, 3, 3
        
    elif (3 <= row < 6 and 0 <= col < 3):
        
        min_x, min_y, max_x, max_y = 3, 0, 6, 3
        
    elif (6 <= row < 9 and 0 <= col < 3):
        
        min_x, min_y, max_x, max_y = 6, 0, 9, 3
        
    if (0 <= row < 3 and 3 <= col < 6):
        
        min_x, min_y, max_x, max_y = 0, 3, 3, 6
        
    elif (3 <= row < 6 and 3 <= col < 6):
        
        min_x, min_y, max_x, max_y = 3, 3, 6, 6
        
    elif (6 <= row < 9 and 3 <= col < 6):
        
        min_x, min_y, max_x, max_y = 6, 3, 9, 6
        
    if (0 <= row < 3 and 6 <= col < 9):
        
        min_x, min_y, max_x, max_y = 0, 6, 3, 9
        
    elif (3 <= row < 6 and 6 <= col < 9):
        
        min_x, min_y, max_x, max_y = 3, 6, 6, 9
        
    elif (6 <= row < 9 and 6 <= col < 9):
        
        min_x, min_y, max_x, max_y = 6, 6, 9, 9
        
    for x in range(min_x, max_x):
        
        for y in range(min_y, max_y):
            
            #print(grid[x][y].get_pos())
            
            if (grid[x][y].get_value() == number and grid[x][y].get_pos() != (row, col) and number > 0):
                
                #print(grid[x][y].get_pos())
                
                return False

    for x in grid[row]:
         
        if (x.get_value() == number and x.get_pos() != (row, col) and number > 0):
            
            return False
        
    for x in range (len(grid)):
        
        if (grid[x][col].get_value() == number and grid[x][col].get_pos() != (row, col) and number > 0):
            
            return False
            
    return True
    
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
                    
                    if is_valid_num(grid, self.row, self.col, self.value):
                        
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
                    
                    if is_valid_num(grid, self.row, self.col, self.value) or self.value < 1:
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
        
        self.neighbours = update_moves(matrix, self.row, self.col)
        
            
    # Less than operator
    def __lt__ (self, other):
        return False
    
def get_clicked_pos(pos, rows, width):
	gap = width // rows
	y, x = pos

	row = y // gap
	col = x // gap

	return row, col
        
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
            
def draw(Game, grid, rows, width):
    
    Game.fill(white)

    for x in grid:
        
        for square in x:
            
            square.draw(Game)


    draw_grid(Game, rows, width)
    
    pygame.display.update()

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
                
                row, col = get_clicked_pos(pos, rows, width)
                
                if (row < rows):
                
                    spot = grid[row][col]
                                    
                    #spot.find_nearby_spots(grid)
                    
                    spot.find_nearby_spots(grid)
                    
                    spot.get_clicked(grid, True)
                    
            if pygame.mouse.get_pressed()[2]:
            
                pos = pygame.mouse.get_pos()
                
                row, col = get_clicked_pos(pos, rows, width)
                
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
                    
                    grid = make_grid(rows, width)
                    
    
main(Game, 9, 801)