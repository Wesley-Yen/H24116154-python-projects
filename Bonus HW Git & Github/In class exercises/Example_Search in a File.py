pattern = "Pineapple-pen"
line_num = 0
result = []

with open("C:/Users/yenwe/Desktop/PYTHON/In class exercises/ppap.txt","r") as fr :
    for line in fr :
        if line.find(pattern) != -1 :
            col_num = line.index(pattern)
            found = "[line-%d, column-%d]"%(line_num,col_num)
            result += [found]
        line_num += 1

with open("C:/Users/yenwe/Desktop/PYTHON/In class exercises/ppap_pattern.txt","w") as fw :
    fw.writelines(result)