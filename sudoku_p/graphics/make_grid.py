if __name__ == "__main__":
    import generate_grid as main

def make_grid(rows, width):
    
    grid = []
    
    for x in range(rows):
        
        temp = []
        
        for y in range(rows):
            
            # Create square objects
            spot = main.square(0, x, y, (width // rows), rows)
            
            temp.append(spot)
            
        grid.append(temp)

    return grid