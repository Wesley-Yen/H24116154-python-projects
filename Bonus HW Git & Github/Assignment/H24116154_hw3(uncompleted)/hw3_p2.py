#### Problem 2: Evaluation of Polynomial Strings

answer = input("Input polynomials : ")
ans = answer.strip(" ")


x = float(input("Input the value of x : "))

#### Polynomials components : ( (+/-) -> coefficient -> "*" -> variable x -> "^" -> power ) constitute a full loop

#### 將多項式ans依 (+/-) 分割成每一項並儲存

# 先依 + 分割
plus_divided = ans.split("+")
print(plus_divided)


#### 將每一項化為初始化串列 [+1/-1 , coefficient , variable , power]

## eg. 3*X^8   初始化為 [1 , 3 , X , 8]
## eg. -8*X^2  初始化為 [-1 , 8 , X , 2] 

initialization_list = ["sign","coefficient","variable","power"]

each_initialization = []

for items in plus_divided :


    ## handle with "coefficient"
    for index in range(0,len(items)) :
        if items[index].isdigit() :

            start = index
            i = index
            
            if items[i] == "*" and i < len(items) :  # 係數後面必接"*"
                end = i
                operation_coef = initialization_list.replace("coefficient",str(items[start:end]))
                start = end + 1 # 更新start
                break
            else :
                 i += 1

    if i == len(items) - 1 :
        operation_coef = initialization_list.replace("coefficient",str(1))

    print(operation_coef)

    ## handle with "variable"
    for index in range(0,len(items)) :    
        if items[index] == "X" :
            operation_var = operation_coef.replace("variable",x)
            break
    print(operation_var)
    ## handle with "power"
    for index in range(0,len(items)) :   

        start = index
        i = index 

        if items[i] == "^" and i < len(items) : # 次方後面必接數字
            end = i + 1
            operation_power = operation_var.replace("power",items[start+1:end])
            break
    print(operation_power)
    ## handle with "sign"
    while True :

        if items[0] == "-" :
            operation = operation_power.replace("sign",-1)
            break
        else :
            operation = operation_power.replace("sign",1)
            break
    print(operation)
           
        
        
        
    each_initialization.append(operation)
                

print(each_initialization)



