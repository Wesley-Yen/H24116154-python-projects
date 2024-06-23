def parse_matrix(input_str):
    """將用戶輸入的矩陣字串轉換為字典，並進行格式檢查"""
    try:
        rows = input_str.split('|')
        matrix = {}
        row_length = None
        for i, row in enumerate(rows):
            elements = row.split(',')
            if row_length is None:
                row_length = len(elements)
            elif row_length != len(elements):
                raise ValueError("每行的元素數量必須一致")
            for j, value in enumerate(elements):
                # 以元組(tuple)當鍵值
                matrix[(i, j)] = int(value)
        if len(rows) != row_length:
            raise ValueError("矩陣必須是方陣")
        return matrix, row_length
    
    except ValueError as e:
        print(f"輸入格式錯誤: {e}")
        return None, None

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
    while True:
        # 從用戶處獲取輸入矩陣
        U_input = input("Enter matrix U: ")
        V_input = input("Enter matrix V: ")
        
        # 解析輸入並轉換為字典
        U, n = parse_matrix(U_input)
        V, m = parse_matrix(V_input)
        
        # 如果解析成功且矩陣大小相同，則進行矩陣乘法
        if U is not None and V is not None and n == m:
            # 計算矩陣乘積
            M = matrix_multiplication(U, V, n)
            
            # 打印結果
            print("M = U x V")
            print_matrix(M, n)
            break
        else:
            print("請重新輸入正確格式的矩陣\n(input the square matrix with rows separated by | and elements separated by ,)")

if __name__ == "__main__":
    main()
