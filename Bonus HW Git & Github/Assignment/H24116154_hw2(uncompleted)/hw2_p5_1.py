# Fibonacci Sequence

# 確保使用者輸入正確的參數
while True :
    n = input("Please input an integer number: ")
    if n.isdigit() :
        if int(n) >= 0 :
            n = int(n)
            break            
    else :
        print("Please enter the valid range of n (n is a nonnegative integer)")

Fn_2 = 0   # 第i-2個數字 並初始化,定義第0項為0  i.e. F0 = 0
Fn_1 = 1   # 第i-1個數字 並初始化,定義第1項為1  i.e. F1 = 1
i = 2      # 初始化,表當前正在計算的斐波那契數列的第 i 個數字

while i <= n :
    Fn = Fn_2 + Fn_1  # Fn = Fn-2 + Fn-1
    Fn_2 = Fn_1       # update Fn_2 by assigning Fn_1 from the previous iteration 
    Fn_1 = Fn         # update Fn_1 by assigning Fn   from the previous iteration 

    i+=1  # update i

if n == 0 :
    print("The 0-th Fibonacci sequence number is : 0")

elif n == 1 :
    print("The 1-th Fibonacci sequence number is : 1")

else :
    print("The %d-th Fibonacci sequence number is : %d"%(n,Fn))