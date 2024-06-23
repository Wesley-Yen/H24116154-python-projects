def parse_matrix(input_str):
    """將用戶輸入的矩陣字串轉換為字典"""
    rows = input_str.split('|') 
    matrix = {}
    for i, row in enumerate(rows):
        for j, value in enumerate(row.split(',')):
            matrix[(i, j)] = int(value)
    return matrix

def matrix_multiplication(U, V, n):
    """計算兩個方陣的乘積，結果存儲在字典中"""
    M = {}
    
    for i in range(n):
        for j in range(n):
            M[(i, j)] = 0
            for k in range(n):
                M[(i, j)] += U[(i, k)] * V[(k, j)]
    
    return M

def print_matrix(M, n):
    """打印字典形式存儲的矩陣"""
    for i in range(n):
        row = [M[(i, j)] for j in range(n)]
        print(row)

def main():
    # 從用戶處獲取輸入矩陣
    U_input = input("Enter matrix U: ")
    V_input = input("Enter matrix V: ")
    
    # 解析輸入並轉換為字典
    U = parse_matrix(U_input)
    V = parse_matrix(V_input)
    
    # 獲取矩陣大小（假設是方陣）
    n = int(len(U) ** 0.5)
    
    # 計算矩陣乘積
    M = matrix_multiplication(U, V, n)
    
    # 打印結果
    print("M = U x V")
    print_matrix(M, n)

if __name__ == "__main__":
    main()
