import find_moves.valid_move as valid_move

def update_moves (grid, row, col):
    
    moves = []
    
    for x in range(1, 10):
        
        if (valid_move.is_valid_num(grid, row, col, x)):
            
            moves.append(x)
            
    return moves