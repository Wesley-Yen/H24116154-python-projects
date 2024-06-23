###### Grid Editor

#### Step 1. The function of ensuring the user to input the valid value

def get_valid_size() :
    while True :
        size = input("Enter the size of the grid : ")
        if size.isdigit() and int(size) > 0 :
            size = int(size)
            break
        else :
            print("Please enter the positive integer ! ")
            continue

    return size

def get_valid_coord(size) :
    while True :
        coord = input("Enter the cell coordinates to edit : ")
        if coord.lower() == "done" :
            coord = coord.lower()
            break

        elif coord.count(",") == 1 :
            check = coord.split(",") # check = ["row","col"]
            check_row = check[0]
            check_col = check[1]
                
            if check_row.isdigit() and check_col.isdigit() :

                if (0 <= int(check_row) < size) and (0 <= int(check_col) < size) :
                    break
                else :
                    print("The cell coordinate is \'Out-of-range\'")
                    print("Please enter again!")
                    print()
                    continue
            else :
                print("Please enter the positive integer of cell coordinate !")
                print()
                continue

        else :
            print("Please enter the valid format : row,col ")
            print()
            continue

    return coord

def get_valid_new_value() :

    while True :
        new_value = input("Enter the new value for the cell : ")
        if len(new_value) == 1 :
            break
        else :
            print("Value Error ! Please enter the \'single\' value")
            print()
    return new_value

#### Step 2. generate the matrix and then modified it

def grid_matrix_generation(size) :
    grid = ["_" for _ in range(size**2)] # eg. grid = ["_","_","_",...]

    grid_matrix = []
    for row in range(size) :
        col = row + size
        grid_matrix.append(grid[row:col])  # eg. grid_matrix = [["_","_","_"],["_","_","_"],...]

    return grid_matrix

def modified_grid_matrix(coord,new_value,grid_matrix) :

    # grid_matrix = grid_matrix_generation(size)

    coord_list = coord.split(",")  # coord = ["row","col"]
    row = int(coord_list[0])
    col = int(coord_list[1])
    grid_matrix[row][col] = new_value
    
    return grid_matrix

#### Step 3. print the initial grid or modified grid

def print_initial_grid(size) :
    grid_matrix = grid_matrix_generation(size)
    for row in grid_matrix :
        print(" ".join(row))
    ''' eg. size = 3    _ _ _
                        _ _ _
                        _ _ _  '''

def print_modified_grid(coord,new_value,grid_matrix) :
    grid_matrix = modified_grid_matrix(coord,new_value,grid_matrix)
    for row in grid_matrix :
        print(" ".join(row))
    ''' eg. size = 3    _ _ _
                        _ X _
                        B _ _  '''


# Step 4. The execution of the main program
if __name__ == "__main__" :

    # Get the valid parameter
    size = get_valid_size()

    round = 1 # To record what number of input this is
    # grid_matrix = [] # initialization
    grid_matrix = grid_matrix_generation(size)

    while True :
    
        if round == 1 :
            print_initial_grid(size)
            round += 1    
        
        coord = get_valid_coord(size)   
    
        if coord == "done" :
            print()
            break

        else :
            new_value = get_valid_new_value()

            grid_matrix = modified_grid_matrix(coord,new_value,grid_matrix)  # update the parameter of the function
            print_modified_grid(coord,new_value,grid_matrix)

            if coord == "done" :
                print()
                break
            else :
                continue

