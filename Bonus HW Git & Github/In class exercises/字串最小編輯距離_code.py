#### 計算兩個字串之間的最小編輯距離（minimum edit distance）

def minDist(w1, w2):

    ## step 1. 計算了兩個字串的長度, 並分別加上 1，因為我們將要建立一個多維列表來存儲動態規劃的結果, 這樣可以避免索引超出範圍的問題
    l1, l2 = len(w1) + 1, len(w2) + 1
    dp = []

    ## step 2. 初始化動態規劃表, 將其填充為全 0
    for i in range(l1):
        dp.append([0] * l2)

    ## step 3. 初始化動態規劃表的第一列, 表示從空字串到 w1 字串的最小編輯距離, 即插入操作的次數    
    for i in range(l1):  
        dp[i][0] = i

    ## step 4. 初始化動態規劃表的第一行, 表示從空字串到 w2 字串的最小編輯距離, 即刪除操作的次數
    for j in range(l2):  
        dp[0][j] = j

    ## 對於每一對字元 (w1[i], w2[j]), 比較以下三種操作的次數    
    for i in range(1, l1):
        for j in range(1, l2):


            dp[i][j] = min(dp[i-1][j] + 1, # 插入操作
                           dp[i][j-1] + 1, # 刪除操作
                           dp[i-1][j-1] + (w1[i-1] != w2[j-1])) # 替換操作 (如果 w1[i-1] 不等於 w2[j-1], 則需要進行替換操作, 否則不需要)

    ## 返回動態規劃表中右下角元素，這個元素表示將 w1 轉換為 w2 所需的最小編輯距離     
    return dp[-1][-1]

print(minDist("cafe", "coffee"))
print(minDist("intention", "execution"))