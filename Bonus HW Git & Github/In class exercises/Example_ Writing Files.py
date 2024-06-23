limit = int(input("Enter the powers : "))
header = "Table pf Powers from 1 to %d\n"%limit
bar = "="*len(header) + "\n\n"

with open("C:/Users/yenwe/Desktop/table-of-powers.txt","w") as f :
    f.write(header)
    f.write(bar)

    for i in range(1,limit+1) :
        f.write("%3d  %5d  %5d\n"%(i,i**2,i**3))

