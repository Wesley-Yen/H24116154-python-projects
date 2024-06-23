def candy_crush(board):
    # determine the row and column
    row = len(board)
    col = len(board[0])
    endgame = False

    while not endgame:
        endgame = True
        # 存放可消除的座標
        coor = set()
        # 檢查可消除的糖果，並將座標加入 coordinate 的 set 中
        for i in range(row):
            for j in range(col):
                candy = board[i][j]
                # zero case
                if candy == "0":
                    continue

                # veritcal 
                if j+2 < col and board[i][j+1] == board[i][j+2] == candy:
                    # 利用 union 函數取聯集
                    coor = coor.union({(i, j), (i, j+1), (i, j+2)})
                # horizontal
                if i+2 < row and board[i+1][j] == board[i+2][j] == candy:
                    coor = coor.union({(i, j), (i+1, j), (i+2, j)})
        
        # 消除後為0
        for x, y in coor:
            board[x][y] = "0"
            endgame = False
        # drop candy
        for j in range(col):
            dis = 0
            for i in range(row-1, -1, -1):
                # 計算需落下幾格
                if board[i][j] == "0":
                    dis += 1
                # 遇到非0的糖果 & 距離>0
                elif dis > 0:
                    board[i+dis][j] = board[i][j]
                    board[i][j] = "0"
                    

    return board

filename1 = "candy_input1.txt"
filename2 = "candy_input2.txt"

# load input1
with open(filename1, "r") as f:
    board1 = []
    for line in f.readlines():
        line=line.strip("\n")
        board1.append(line.split(","))
    f.close()

# load input2
with open(filename2, "r") as f:
    board2 = []
    for line in f.readlines():
        line = line.strip("\n")
        board2.append(line.split(","))
    f.close()

# update new board
result1 = candy_crush(board1)
result2 = candy_crush(board2)

# write in txt
path1 = "candy_output1.txt"
path2 = "candy_output2.txt"

with open(path1, "w") as f:
    for l in result1:
        for n in l:
            f.writelines(n)
            f.writelines(",")
        f.writelines("\n")

with open(path2, "w") as f:
    for l in result2:
        for n in l:
            f.writelines(n)
            f.writelines(",")
        f.writelines("\n")