#### make sure the user input the valid parameter
while True :
    x = input("Enter an integer (x>1) : ")
    if x.isdigit() and int(x) > 1 :
        x = int(x)
        break
    else :
        print("Please enter an integer greater than 1")
        continue

#### Establish the list to store Fibonacci sequence
Fn_2 = 0
Fn_1 = 1
F_list = []
while True :
    Fn = Fn_1 + Fn_2
    Fn_2 = Fn_1
    Fn_1 = Fn
    F_list.append(Fn)

    if Fn > x :
        break
print(F_list)

#### Check if x is in the Fibonacci sequence or not
trigger = True
if x in F_list :
    i = 0
    
    while i <len(F_list) :
        if x == F_list[i] :
            print("%d is the %d-th Fibonacci sequence"%(x,i))
            trigger = False
            break
        
        i += 1
if trigger :
    print("not")

#### Establish the list to store prime number
count = x # 利用x來控制輸出到""第幾個質數""
i = 2
prime_list = []

while True :
    if i == 2 :
        prime_list.append(i)
        count -= 1
    else :
        j = 2
        while j < i :
            trigger = True
            if i%j == 0 :
                trigger = False
                break
            j += 1

        # check if i is prime number or not
        if trigger :
            prime_list.append(i)
            count -= 1

    if count == 0 :
        break
    
    i += 1

print(prime_list)

print("The %d-th prime is %d"%(x,prime_list[-1]))
