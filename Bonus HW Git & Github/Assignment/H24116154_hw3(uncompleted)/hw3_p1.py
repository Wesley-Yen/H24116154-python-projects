#### Problem 1: Find the Last ID of Leaving a Round Table

#### 判斷使用者輸入正確的參數
while True :
    n = input("Input the total number of students (n>0) : ")
    if n.isdigit() and int(n) > 0 :
        n = int(n)
        break

    else :
        print("Please enter the positive integer (n>0) !")
        continue

#### 建立一串列儲存Student ID

sid = [] # initialization
for i in range(1,n+1) :
    sid.append(i)
# print(sid)

#### 將order中的數字迭代地填入circulation_1st中

order = [1,2,3]           # 每3個一循還
circulation_1st = []      # 表示"第1次循環"

# 迴圈歷遍sid的總長度
for i in range(0,len(sid)) :

    # 利用i%len(order)來判斷應該要填入order中哪一個元素
    circulation_1st.append(order[i%len(order)])

# print(circulation_1st)

#### 算出總共要進行幾次循環

## 想法 : 
# step1. 進行每次循環前先讓其從1開始循環 (計算deduction)
# step2. 計算出現3的個數 == ""扣除完deduction後的長度"" 除以 len(order)的 ""商數"" 
# step3. 將 ""扣除完deduction後的長度"" 與step2.中所得之數字相減
# step4. 最後再補上之前多扣的數字 (計算revise)

#----------------------------------- ILLUSTRATION -----------------------------------#

# 以 n = 11 ,order = [1,2,3]為例  i.e.每3個一循環

# 1st circulation : [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2]
# 2nd circulation : [3, 1, 0, 2, 3, 0, 1, 2, 0, 3, 1]
# 3rd circulation : [0, 2, 0, 3, 0, 0, 1, 2, 0, 0, 3]
# 4th circulation : [0, 1, 0, 0, 0, 0, 2, 3, 0, 0, 0]
# 5th circulation : [0, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0]
# 6th circulation : [0, 3, 0, 0, 0, 0, 1, 0, 0, 0, 0]
# 7th circulation : [0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0]

# 第1次循環:長度為11
# step1. 11-0 = 11 (第1次循環必從1開始, 故deduction = 0)
# step2. 11//3 = 3 (表示3重複出現3次)
# step3. 11-3 = 8  (扣除3出現的個數)
# step4. 8+0 = 8   (因deduction = 0, 故不會多扣)

# 第2次循環:長度為8
# step1. 8-1 = 7   (由於 11%3 = 2 (第1次循環由1,2作結尾), 故第2次循環從3開始, deduction = 3 - 11%3 = 1)
# step2. 7//3 = 2  (表示3重複出現2次)
# step3. 7-2 = 5   (扣除3出現的個數)
# step4. 5+0 = 8   (由於第2次循環從3開始, 在下一次循環會被扣除, 故不用補齊)

# 第3次循環:長度為5
# step1. 5-2 = 3   (由於 (8-1)%3 = 1 (第2次循環由1作結尾), 扣除1是因為第2次循環從3開始, 故第2次循環從2,3開始, deduction = 3 - 7%3 = 2)
# step2. 3//3 = 1  (表示3重複出現1次)
# step3. 3-1 = 2   (扣除3出現的個數)
# step4. 2+1 = 3   (由於第3次循環從2開始, 多扣1個2, 需補齊)

## 其規律就是 remainder = [0,1,2]
# 當remainder=0時, 表示由3結尾, 故下一次循環必從1開始, 故不用扣, 當然也不用補數字 deduction = 0 , revise = 0
# 當remainder=1時, 表示由1結尾 (ending = 1), 故下一次循環從2開始, deduction = 3-1 = 2 , revise = 3-1-1 = 0
# 當remainder=2時, 表示由2結尾 (ending = 2), 故下一次循環從3開始, deduction = 3-2 = 0 , revise = 3-2-1 = 0

## Generalization : order = [1,2,3,......,n] -> remainder = [0,1,2,......,n-1]
# when remainder = 0 , deduction = 0 , revise = 0
# when remainder = k != 0 (i.e. ending = k) , deduction = n - k , revise = n - k -1

#------------------------------------------------------------------------------------#

length = n
stored_length = []
i = 0          # 初始化:表第1次循環
revise = 0     # 補齊多扣的數字
deduction = 0  # 讓每次循環皆從1開始

## 建立for迴圈儲存 length % len(order) 所有可能的餘數
remainder = []    
for j in range(0,len(order)) :
    remainder.append(order[j]%len(order))

while length != 1 :

    stored_length.append(length) 
    i += 1

    length -= deduction                   ## step1.
    last_circulation = length  # 讓其繼承上一次循環之長度並且要從1開始, 故接在 k -= deduction 之後                   

    remove_times = length // len(order)   ## step2.
    length -= remove_times                ## step3.

    length += revise                      ## step4.

    # 藉由判斷 ""上一次循環且從1開始"" 的長度除以len(order)的餘數決定上一次循環是多少結尾 
    for j in remainder :
        if j == last_circulation % len(order) :
            ending = j
            break
    # 藉由條件判斷 ""下一次循環"" 之 deduction 和 revise 為多少
    if ending == 0 :
        deduction = 0          
        revise = 0

    else :
        deduction = len(order) - ending
        revise = len(order) - ending - 1


stored_length.append(length)
print(stored_length)

times = len(stored_length)


#### 找出第k次循環的list

## 其中 ""第k+1次"" 循環的 ""第1個元素"" 會受 ""第k次"" 循環的 ""最後一個元素"" 影響 !
## 而且凡是第k次循環中出現 ""3"" 者, 進行第k+1次循環時會變成0, 並且之後的循環皆會繼承之 !

each_circulation = []                       # initialization
each_circulation.append(circulation_1st)    # 儲存第1次循環

stored_start = []

# 最外層迴圈負責歷遍每次循環
for i in range(0,times-1) :

    circulation_k = list(each_circulation[i])

    ### 針對circulation_k進行修改

    ## 先初始化每次循環的串列 : (1) 將上一次循環出現之 3 或 0 全部替換成 0 ; (2) 反之, 替換成"X"
    for j in range(0,n) :
        if (each_circulation[i][j] == len(order)) or (each_circulation[i][j] == 0) :           
            circulation_k[j] = 0
        else :
            circulation_k[j] = "X"

    ## 再處理該次循環是多少開頭
            
    # 第一次循環(初始化)        
    if i == 0 : 
        start = 1                                # 表當前循環多少開頭, 初始化表1開頭
        ending = stored_length[i] % len(order)   # 表當前循環多少結尾, 若為0則表示3結尾
        stored_start.append(start)
        if ending == 0 :
            start = 1              # 下一次循環是從1開始
        else :
            start = ending + 1     # 下一次循環是從ending+1開始

    # 第二次或以上的循環
    else :
        if start != 1 : # 不從1開始
            ending = (stored_length[i] - (len(order) - start) - 1) % len(order)
            if ending == 0 :
                start = 1
            else :
                start = ending + 1

        else :          # 從1開始
            ending = (stored_length[i]) % len(order)
            if ending == 0 :
                start = 1           # 下一次循環是從1開始
            else :
                start = ending + 1  # 下一次循環是從ending+1開始
        
    stored_start.append(start)

    ## 先依序填入當次循環是由多少開頭, 最後再將order迭代地填入剩餘空格之中
    begin = start
    index = 0
    for h in range(0,n) :
        
        if 1 < begin < len(order) : # 不從1開始
            if circulation_k[h] != 0 and (not circulation_k[h].isdigit()) :
                circulation_k[h] = begin
                begin += 1
            
        elif begin == len(order) : 
            if circulation_k[h] == "X" :
                circulation_k[h] = begin
                begin = 1 

        elif begin == 1 :           # 從1開始
            # 歷遍每個位置, 依序將order的順序填入
            for g in range(0,n) :
                if circulation_k[g] == "X" :
                    circulation_k[g] = order[index%len(order)] 
                    index += 1  

    ## 將每次循環的結果存入二維陣列中
    each_circulation.append(circulation_k) 

# print(stored_start)
print(each_circulation)            

#### 印出結果

last_circulation = each_circulation[len(each_circulation)-1]
for i in range(0,len(sid)) :
    if last_circulation[i] != 0 :
        print("The last ID is : %d"%(sid[i]))
        break