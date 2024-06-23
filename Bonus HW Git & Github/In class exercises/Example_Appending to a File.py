msg = input("To be logged : ")

while msg :
    f = open("log.txt","a")
    f.write(msg+"\n")
    msg = input("To be logged : ")
    f.close()