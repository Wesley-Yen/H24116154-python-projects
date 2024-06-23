# 定義二維串列
def initial_grid(s) :

    grid = []
    i = 0
    while i < s**2 :
        grid.append("_")
        i += 1
    
    grid_str = ""
    i = 0
    while i < s**2 :
        row = grid[i:i+s]
        grid_str += " ".join(row) + "\n"
        i += s
    
    print(grid_str)

    grid_matrix = []
    i = 0
    while i < s**2 :
        row = grid[i:i+s]
        grid_matrix.append(row)
        i += s
        
    return grid_matrix    


while True :
    s = input("Enter the size of the grid : ")
    if s.isdigit() and int(s)>0 :
        s = int(s)
        initial_grid(s)

        count = 0 # 計算輸入次數

        while True :
            coord = input("Enter the cell coordinates to edit : ")
            new = input("Enter the new value for the cell : ")
        
            if coord.lower() == "done" :
                break
            else :
                stored_list = coord.split(",")
                row = int(stored_list[0])
                col = int(stored_list[1])

                if count == 0 :
                    previous = initial_grid(s)
                    previous[row][col] = new

                    previous_str = ""

                    i = 0
                    while i < s :
                        j = 0
                        while j < s :
                            previous_str += previous[i][j] + " "
                            j += 1
                        previous_str += "\n"
                        i += 1
                    
                    print(previous_str)
                    count += 1
                
                else :
                    previous[row][col] = new
                    previous_str = ""
                    i = 0
                    while i < s :
                        j = 0
                        while j < s :
                            previous_str += previous[i][j] + " "
                            j += 1
                        previous_str += "\n"
                        i += 1
                    
                    print(previous_str)
                                   
                continue
        break
                
    else :
        print("Please enter the positive integer!")
        continue