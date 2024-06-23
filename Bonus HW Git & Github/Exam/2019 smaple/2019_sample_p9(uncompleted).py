def find_missing_ranges(nums, lower, upper): # 這行定義了一個函式 find_missing_ranges，它有三個參數：nums 是一個已排序的整數列表，lower 是下界，upper 是上界。
    
    result = []       # 用於存儲找到的缺失範圍。
    prev = lower - 1  # 初始化一個變數 prev，其值為下界 lower 減去 1。這樣做是為了確保我們能夠捕獲下界之前的任何缺失範圍。

    for i in range(len(nums) + 1): # 它將遍歷整個列表 nums 以及末尾的一個虛擬元素（上界之後的一個元素）。
        
        # 如果迴圈索引 i 小於列表 nums 的長度，則將 current 設置為列表 nums 中索引為 i 的元素。
        if i < len(nums):
            current = nums[i]
        #否則，current 設置為上界 upper 加 1。
        else:
            current = upper + 1

        # 檢查前一個元素與當前元素之間是否存在缺失範圍。
        if prev + 1 <= current - 1:
            
            # 如果前一個元素與當前元素之間的差值為 1，則說明只缺失了一個數字，直接將該數字添加到結果列表中。
            if prev + 1 == current - 1:
                result.append(str(prev + 1))
            # 如果前一個元素與當前元素之間的差值大於 1，則說明存在一個範圍的缺失，將這個範圍的起始和結束值（以字串形式）添加到結果列表中。
            else:
                result.append(str(prev + 1) + "->" + str(current - 1))

        # 將當前元素設置為前一個元素，以便在下一次迭代中使用。
        prev = current

    return result # 返回找到的所有缺失範圍。

# Test the function
nums = [0,33,66,88]
lower = 11
upper = 77
print(find_missing_ranges(nums, lower, upper))

