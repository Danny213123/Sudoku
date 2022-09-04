# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 00:54:15 2022

@author: danny
"""

def set_next(grid):
    global last
    
    previous_position = None
    
    for x in range(len(grid)):
        
        for y in range(len(grid[x])):
            
            temp = grid[y][x]
            
            if (previous_position != None):
                
                previous_position.set_next(temp)
                
                #print(previous_position.get_pos(), previous_position.next.get_pos())
                
                if (not temp.st):
                    previous_position = temp
                    
                    last = temp
                
            else:
                
                if (not temp.st):
                    previous_position = temp

def set_root(grid):
    
    temp_found = False
    
    global first
    
    previous_position = grid[0][0]
    
    for x in range(len(grid)):
            
            for y in range(len(grid[x])):
                
                temp = grid[y][x]
                
                temp.set_root((previous_position))
                
                if (not temp_found and not temp.st):
                    first = temp
                    temp_found = True
                
                if (not temp.st):
                    previous_position = temp
                
                #print(temp.get_pos(), temp.root.get_pos())

def solve_sudoku(grid, draw):
    
    # pseudo
        
    # if after update click and click is equal to valid_moves[0], set current grid to 0, move back 1
    
    i = 0
    
    set_root(grid)
    
    set_next(grid)
    
    cur_pos = first
    
    end_pos = last
    
    while True:
    
        #print(i)
        
        #print(cur_pos.get_pos(), cur_pos.value)
        
        cur_pos.find_nearby_spots(grid)
        
        #print(cur_pos.get_pos())
        
        if (not (cur_pos.st)):
            
            cur_pos.get_clicked(grid, False)
        
        if (cur_pos.value == 0):
            
            if (cur_pos is not first):
                cur_pos = cur_pos.root
            
        elif (cur_pos.visited and cur_pos.value == cur_pos.neighbours[0]):
            
            cur_pos.set_value(0)
            
            cur_pos.set_visited(False)
            
            if (cur_pos is not first):
                cur_pos = cur_pos.root
            
        else:
            
            cur_pos.set_visited(True)
            
            cur_pos = cur_pos.next

        #draw()
        
        if (end_pos.value > 0):
            return
        
        i += 1
        
        