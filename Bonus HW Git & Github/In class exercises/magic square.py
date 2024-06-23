while True :
    n = input("Please enter a postive integer (repesented n x n table) : ")
    if n.isdigit() :
        n = int(n)
        values_str = input("Please enter values sperated with a space to repersent each element in n x n table : ")
        if len(values_str.split(" ")) == n**2 :
            values_list = values_str.split(" ")
            
            i = 0
            while i < len(values_list) :
                values_list[i] = int(values_list[i])
                i += 1
            break
        else :
            print("Please enter the correct numbers of values related to n")

    else :
        print("Please enter a positive integer !")
        continue

## initialize the matrix
matrix = []
i = 0
while i < n**2 :
    end = i + n
    matrix.append(values_list[i:end])
    i += n
print(matrix)

# maxtrix = 16 3 2 13 5 10 11 8 9 6 7 12 4 15 14 1


## check each row, col, diagonal
row = 0
col = 0

row_sum_list = []

col_sum_list = [0]*n

diag_sum_list = [0]*2
lt_to_rb_diag_list = [0]*n   # diagnol sum (left-top to right-bottom)
lb_to_rt_diag_list = [0]*n   # diagnol sum (left-bottom to right-top)

criteria = sum(matrix[0])

while True :

    ## check row sum 
    while row < n :
        row_sum_list.append(sum(matrix[row]))
        row += 1
    print(row_sum_list)

    ## check col sum
    while col < n : 
        row = 0
        while row < n : 
            col_sum_list[col] += matrix[row][col]
            row += 1
        col += 1
    print(col_sum_list)
    
    ## check diagnol sum
    
    # diagnol sum (left-top to bottom-right)
    row = 0
    while row < n :
        lt_to_rb_diag_list[row] += matrix[row][row]
        row += 1
    diag_sum_list[0] += sum(lt_to_rb_diag_list)
    

    # diagnol sum (left-bottom to right-top)
    row = 0
    while row < n :
        col = n - row
        lb_to_rt_diag_list[row] += matrix[row][col-1]  
        row += 1
    diag_sum_list[1] += sum(lb_to_rt_diag_list)

    print(diag_sum_list)

    # check if the matrix is magic square or not 
    if (sum(row_sum_list)//n == criteria) and (sum(col_sum_list)//n == criteria) and (sum(diag_sum_list)//2) :
        print("The matrix is the magic square")

    else :
        print("The matrix is not a magic square")
    
    break

#### Solution 2.

dim = len(matrix[0])
sum_list = []

# Row sum
i = 0
while i < dim :
    sum_list.append(sum(matrix[i]))
    i += 1

# Column sum
j = 0
colsum = [0]*len(matrix)
while j < dim :
    i = 0
    while i < dim :
        colsum[j] += matrix[i][j]
        i += 1
    j += 1
sum_list.extend(colsum)

# Diagonal Sum (left-top to right-bottom)
i = 0
dlsum = 0
while i < dim :
    dlsum += matrix[i][i]
    i += 1
sum_list.append(dlsum)

# Diagonal Sum (left-bottom to right-top)
i = 0
drsum = 0
# range(dim-1,-1,-1) 生成的是一個從 dim-1 到 0 的遞減序列, 即從右下角到左上角對角線上元素的索引
diag_indices = range(dim-1,-1,-1) 
while i < len(diag_indices) :
    # diag_indices[i] 是對角線元素的行索引, i 是對角線元素的列索引
    drsum += matrix[diag_indices[i]][i]
    i += 1
sum_list.append(drsum)

if set(sum_list) > 1 :
    print("The matrix is not a magic square")
else :
    print("The matrix is a magic square")
















