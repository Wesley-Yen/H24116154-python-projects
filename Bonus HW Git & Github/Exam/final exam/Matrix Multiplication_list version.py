def parse_matrix(input_str):
    """將用戶輸入的矩陣字串轉換為二維列表"""
    rows = input_str.split('|')
    matrix = [list(map(int, row.split(','))) for row in rows]
    return matrix

def matrix_multiplication(U, V):
    """計算兩個方陣的乘積"""
    n = len(U)
    M = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                M[i][j] += U[i][k] * V[k][j]
    
    return M

def print_matrix(M):
    """打印矩陣"""
    for row in M:
        print(row)

def main():
    # 從用戶處獲取輸入矩陣
    U_input = input("Enter matrix U: ")
    V_input = input("Enter matrix V: ")
    
    # 解析輸入並轉換為二維列表
    U = parse_matrix(U_input)
    V = parse_matrix(V_input)
    
    # 計算矩陣乘積
    M = matrix_multiplication(U, V)
    
    # 打印結果
    print("M = U x V")
    print_matrix(M)

if __name__ == "__main__":
    main()
