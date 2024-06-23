# Christmas Celebration 

#### 判斷使用者輸入正確的參數,並記錄之
while True :
    layers = input("Enter the number of layers (2 to 5) = ")         
    top_side_length = input("Enter the side lengths of the top layer = ")
    groth_rate = input("Enter the growth of each layer = ")             
    trunk_width = input("Enter the trunk width (odd number, 3 to 9) = ")
    trunk_height = input("Enter the trunk height (4 to 10) = ")

    if layers.isdigit() and top_side_length.isdigit() and groth_rate.isdigit() and trunk_width.isdigit() and trunk_height.isdigit() :
        l = int(layers)
        tsl = int(top_side_length)
        gr = int(groth_rate)
        tw = int(trunk_width)
        th = int(trunk_height)
        if (2<=l<=5) and (tw in range(3,10,2)) and (4<=th<=10) :
            break
        else :
            print("""Please enter valid range of integers ! 
                  \nThe number of layers (2 to 5)
                  \nThe trunk width (odd number, 3 to 9)
                  \nThe trunk height (4 to 10)\n""")
    else :
        print("Please enter valid integers !")

######### 處理樹

#### 先計算最底部三角形的寬來決定"空格數"(space number)

## 先將 ""每層三角形的高"" 視為一數列 : 規律 第n層的高度 = 首項 + 公差*(項數-1) - 1(因為頂部重疊) = an + d*(n-1) - 1 (where n != 1)
# 定義:  # l 定義為項數n
        # tsl 定義為首項a1
        # gr 定義為公差d

# 將每層三角形的高儲存
stored_list = []
# 將不斷迭代得到的nh加總會得到總高度total_height
total_height = 0
for i in range(1,l+1) :
    if i == 1 :
        nh = tsl + gr*(i-1)       # 最頂端的三角形其頂部並無重疊!
    else :
        nh = tsl + gr*(i-1) - 1   # 頂部重疊
    
    stored_list.append(nh)
    total_height += nh

## 得到 ""每層三角形的高"" 可用於計算 ""當層三角形中每行的寬度"" (i.e.公差為2, 項數=nh 的等差數列)
# 儲存每層的寬度
stored_each_layer = []
# 儲存當個三角形的最底部
bottom_layer = []
for j in stored_list :
    if j == stored_list[0] :         # 若為最頂部三角形:首項=1
        for k in range(1,j+1) :
            each_layer = 1 + 2*(k-1)
            stored_each_layer.append(each_layer)
            if k == j :             # 當個三角形的最底部
                bottom_layer.append(each_layer)

    else :                           # 反之,首項=3(因為頂部重疊)
        for k in range(1,j+1) :
            each_layer = 3 + 2*(k-1)
            stored_each_layer.append(each_layer)
            if k == j :             # 當個三角形的最底部
                bottom_layer.append(each_layer)

print(stored_each_layer)
######### 印出樹

## 藉由最底部三角形的寬(bottom_width)來決定"空格數"
bw = int(stored_each_layer[len(stored_each_layer)-1])

## 利用迴圈歷遍 ""指定三角形當中的每一行""
for j in range(0,len(stored_each_layer)-1) : # 指定是哪一個三角形  
    sn = (bw-stored_each_layer[j])//2       # space numbers

    # 判別每個三角形的底部和最頂端
    if stored_each_layer[j] == 1 :  # 最頂端        
        print("%s%s%s"%( " "*sn , "#"*1 , " "*sn ))  

    # 利用前面的bottom_layer來判斷當前j是否為每個三角形的底部
    # 並接著判斷當前j的下一項是否為3(若為3表示新的一個三角形,如此能保證j必為當個三角形的最底部)
    elif (stored_each_layer[j] in bottom_layer) and (stored_each_layer[j+1] == 3) :  
       print( "%s%s%s"%( " "*sn , "#"*stored_each_layer[j] , " "*sn ) ) 

    else :  # 三角形內部
        print( "%s%s%s%s%s"%( " "*sn , "#"*1 , "@"*(bw-sn*2-2) , "#"*1 , " "*sn ) )  

## 特別討論最後一行
print("#"*bw)

######### 處理樹幹
# tw 表示樹幹寬度
# th 表示樹幹高度
## 利用""最底部三角形的寬""決定樹幹
sn = (bw-tw)//2   # space numbers

for i in range(0,th) :
    print("%s%s%s"%( " "*sn , "|"*tw , " "*sn ))