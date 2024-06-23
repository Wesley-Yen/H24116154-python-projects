# a x b = a*b
# structure : i x (j-k) = i * (j-k)
# 有3個變數i,j,k
# i 負責歷遍a
# j 與 k 聯動負責歷遍並控制b


j = 9  # initialization
while j >= 1 : # 歷遍b
    i = 9 # initialization

    while i >= 1 : # 歷遍a
        
        # 控制b
        k = 0 # initialization
        while k <= 2 : # 實現 : 以 9 x 9 = 81      9 x 8 = 72      9 x 7 = 63 為例
            print("%d x %d = %d"%(i,(j-k),i*(j-k)),end="\t")   
            
            k += 1 # update k
        
        i -= 1 # update i
        print() 
    
    j -= 3 # update j
    print()