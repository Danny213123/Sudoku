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