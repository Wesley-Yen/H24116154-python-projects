# 要求使用者輸入參數
s = input("Enter a sequence of integers seperated by whitespace: ")
stored_list = s.split(" ")

l = []
for i in stored_list :
    l.append(int(i))

LICS = []

# 初始化
start = -1
end = 1
continuity = []

# 外層迴圈用end歷遍每個要子串列的終點位置
while end < len(l) :

    # 找出所有的遞增序列(無連續性)
    check = 0 # 判別連續性
    if end != len(l) - 1 :
        while start < end :
            start += 1
            if l[start] >= l[start+1] : 
                check = 0
                continuity.append(check)
                continue  
                
            else :
                LICS.append(l[start]) 
                check = 1
                continuity.append(check)
    

    else :
        LICS.append(l[end])
    
                   
    end += 1

print(continuity)
print("Length: %d"%(len(LICS)))    
print("LICS: ",LICS)

