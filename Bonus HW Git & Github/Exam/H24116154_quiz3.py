#### Simple Calculator 

# print a welcome message
print("Welcome to the simple calculator program!")

trigger = True # boolean flag to control the loop
operator = ["+","-","*","/"]
while trigger :
    n1 = input("Enter the first number: ")
    n2 = input("Enter the second number: ")

    n1 = float(n1)
    n2 = float(n2)

    operation = input("Select an airthmetic operation (+, -, *, /): ")
    # 判斷使用者輸入正確的運算符號
    if operation not in operator :
        print("Please enter the right operator \"+\" or \"-\" or \"*\" or \"/\" !")
        continue

    # 進行運算
    if operation == "+" :
        print("Result: %.1f"%(n1+n2))

    elif operation == "-" :
        print("Result: %.1f"%(n1-n2))
    
    elif operation == "*" :
        print("Result: %.1f"%(n1*n2))

    elif operation == "/" :
        if n2 != 0 :
            print("Result: %.1f"%(n1/n2))
        else : # 若被0除,則印出報錯訊息,並跳回輸入數字階段
            print("Enter: Dvision by zero!")
            continue

    # 判斷使用者輸入正確的回答
    while True :
        answer = input("Do you want to perform another calculation? (yes or no): ")
        answer = answer.lower()
        if answer == "yes" :
            break
        elif answer == "no" :
            trigger = False
            print("Goodbye!")
            break
        else :
            print("Please enter \"yes\" or \"no\" !")