# Calendar Generation
# By using Zeller's algorithm

#### 要求使用者正確的輸入年分和月份,並將其做修改
while True :
    year = input("Please input year : ")
    month = input("Please input month : ")
    if year.isdigit() and month.isdigit() :
        Y = int(year)
        m = int(month)

        if m == 1 or m == 2 : # shifted month
            m+=12             # 13 = January or 14 = February
            Y-=1

        break 

    else :
        print("Invalid value!\nPlease enter an integer")

##### Determine the day of the week (指定日期是在一周中的星期幾)
# By formula from Zeller's algorithm : w = ( (13(m+1))//5 + (y//4) + (c//4) + d + y - 2*c) % 7
# centry : c
c = Y//100
# year relative to centry : y = Y - 100*c
y = Y - 100*c
# the day of the month : d (訂為1,因為要找當月月初是星期幾)
d = 1

# Calculate w : (1 = Sunday,..0 = Saturday)
w = ( (13*(m+1))//5 + (y//4) + (c//4) + d + y - 2*c ) % 7

#### Generate calender
label = "Sun Mon Tue Wed Thu Fri Sat"
print(label)

# 先判斷是大月or小月or是否為閏年,並紀錄之
if int(month) in [1,3,5,7,8,10,12] : # 大月有31天
    index = 31

elif int(month) in [4,6,9,11] :      # 小月有30天
    index = 30

elif ((int(year)%4 == 0) and (int(year)%100 != 0)) or (int(year)%400 == 0) : # A leap year        
    index = 29                       # 閏年2月有29天

else : # Not a leap year
    index = 28

# 根據w初始化row1 表示當月月初是在星期幾
if w == 0 :
    row1 = " "*(len(label)-3) + "01"

else :
    row1 = " "*4*(w-1) + "01"

# 特別討論第1行 : row1
date = 2                    # 從當月2號開始討論
l = len(row1)               # 初始化l 表示第1行的長度
while l < (len(label)-1) :  # 根據w所對應的星期數來增加之後的日期,直至Sunday    
    row1 += " "*2 + "%02d"%(date)  # 每多一天:第1行會增加2個空格以及日期(占2格) 共多4格!
    l += 4
    date += 1
     
print(row1)

# 利用 while loop 來歷遍剩下的日期
i = date
while i < (index + 1) :  
    # 星期天對應的值是 0,星期一是 1, ... 星期六是 6
    # w 是當月第一天的星期幾,而 (i + w - 1) 就是當前日期在這一週的位置,故過對 7 取餘數,可以確定是否需要換行
    if (i + w - 1) % 7 == 0 :  # 判斷是否換行(當==0時表示星期天,故需換行)
        print("%02d"%(i))
    else :
        print("%02d"%(i), end="  ")

    i += 1