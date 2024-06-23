###### Minesweeper
import random

#### Prepocessing the Board

# initialization
n = 9 # 1 <= n <= 26

# 初始化字母:利用chr() + ASCII碼 生成字母
letter = [chr(i) for i in range(97,97+n)]
# 初始化數字
number = [str(i) for i in range(1,n+1)]

## Step 1. Intialize the board (n X n)

# 建立一函數:將二維串列board中的元素填入, 並顯示整個面板
def Display_Board(board) :
    
    print(" "*4 + "   ".join(letter))
    print(" "*2 + "+---"*len(letter) + "+")

    for i in range(0,n) : # 外層迴圈歷遍每一列
        print("%s"%number[i],end="")

        j = 0
        for j in range(0,n) : # 內層迴圈歷遍每一行, 並把board二維串列中的值填入
            if len(number[i]) == 1 :
                print(" | %s"%(board[i][j]),end="")
            
            else :  # 處理n>=10的狀況(會造成面板右移)
                if j == 0 :
                    print("| %s"%(board[i][j]),end="")
                else :
                    print(" | %s"%(board[i][j]),end="")

        print(" |",end="")
        print()

        print(" "*2 + "+---"*len(letter) + "+")


## Step 2. Initialize and display the mines 

def Display_Mines() :

    # step1. set the mines  
    mines = []
    while len(mines) <= n :
        mine = random.randint(0,n**2+1)
        if mine not in mines :
            mines.append(mine)

    # step2. put the mines into the grids
    grid = []
    for i in range(1,n**2+1) :
        if i in mines :
            grid.append("X")
        else : 
            grid.append("O")

    # step3. turn the grids into the 2 dimensional list (for the purpose of displaying the board)
    grid_matrix = []
    i = 0
    while i < n**2 :
        grid_matrix.append(grid[i:i+n])
        i += n

    return grid_matrix


## Step 3. Calculate the number of adjacent (within a 9x9 range) mines in each grid

def adjacent_mines_matrix(board) :

    adj_matrix = []
    # next_step=[[-1,0],[0,-1],[0,1],[1,0]]
    for i in range(n) : # check each row
        row = [] # 當前第i列每一行的相鄰地雷數

        for j in range(n) : # check each column
            count = 0 # 相鄰地雷數

            if board[i][j] != "X" :
                # for next in next_step:
                    # next_x=i+next[0]
                    # next_y=j+next[1]
                for dx in [-1, 0, 1] :
                    for dy in [-1, 0, 1] :
                        # 確保不超出邊界且並非當前單元格
                        # next_x=i+dx
                        # next_y=j+dy
                        if 0 <= i+dx < n and 0 <= j+dy < n and (dx != 0 or dy != 0) :
                            if board[i+dx][j+dy] == "X":
                                count += 1
                row.append(count)

            else :
                row.append("X")

        adj_matrix.append(row)

    return adj_matrix


## Step 4. Calculate the numbers of mines left


## Some functions

def welcome_message() :
    welcome_message = "Enter the column follow by the row (ex: a5).\nTo add or remove a flag,add \"f\" to the cell (ex: a5f).\nType \"help\" to show this message again"
    print(welcome_message)
    print()

def warning_message() :
    print("Please enter the valid format ! (Enter the column follow by the row (ex: a5)) ")
    print("And the valid letter (%s~%s) and the valid number (%s~%s) :"%(letter[0],letter[n-1],number[0],number[n-1]))
    print()




if __name__ == "__main__" :

    print("Initial Board:")
    board = [[' ' for _ in range(n)] for _ in range(n)]
    Display_Board(board)

    print()

    mines_board = Display_Mines()

    welcome_message()
    print()

    while True :
        
        answer = input("Enter the cell ( mines left) : ")
        if answer.lower() == "help" :
            welcome_message()
            continue

        elif answer !="" :
            if (answer[0] in letter and answer[1:] in number)  :
                print("ok")
                break
            else :
                warning_message()
                continue
        
        else :
            print("The answer cannot be blank !")
            print()

    print("\nAdjacent Mines:")
    board = adjacent_mines_matrix(mines_board)
    Display_Board(board)