# 輸入參數:金額
n = int(input("Enter the shopping amount : "))

# 確認使用者輸入正確的membership level
while True :
    choose = input("Enter the membership level (Regular or Gold) : ")

    if choose.capitalize() == "Regular" or choose.capitalize() == "Gold" :
        break 
    else :
        print("Invalid  membership level. \nPlease enter \'Regular\' or \'Gold\'")
        

# 判斷金額並給予折扣
if choose.capitalize() == "Regular" :
    if n > 1000 :
        if 1000 < n <= 2000 :
            k = 0.9*n
              
        elif 2000 < n <= 3000 :
            k = 0.85*n
              
        elif 3000 < n :
            k = 0.8*n
            
        print("%s $%.13f"%(choose.capitalize(),k))
              
    else : 
        print("%s $%.1f"%(choose.capitalize(),n))
          
else :
    if n > 1000 :
        if 1000 < n <= 2000 :
            k = 0.85*n
              
        elif 2000 < n <= 3000 :
            k = 0.8*n
              
        elif 3000 < n :
            k = 0.75*n

        print("%s $%.13f"%(choose.capitalize(),k))
              
    else : 
        print("%s $%.1f"%(choose.capitalize(),n))

              
    
