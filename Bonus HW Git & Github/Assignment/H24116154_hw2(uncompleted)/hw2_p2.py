# Finding Perfect Numbers

n = int(input("Please input the range number :"))
print("Perfect numbers:")

i=2 # 初始化,表示從2開始歷遍到n
# 最外層while負責歷遍2到n
while i <= n :

    # 內層while負責找出i的所有因數
    j=1 # 初始化,表示i的因數
    k=0 # 初始化,表示i的因數和
    while j <= i :
        if i%j == 0 : # 判別i的因數有哪些,並將其加總
            k+=j
    
        j+=1 # 歷遍<=i的所有可能因數j

    if k/2 == i :  # 判別是否為完美數
        print(i)

    i+=1
