import math
inc=int(input("Enter number"))
ll=int(input("Enter lower Limit"))
ul=int(input("Enter Upper Limit"))
for i in range (1,ul+1):
    num=math.pow(i, inc)
    if (num>ll) and (num<ul):
        print(num,"is",i,"^",inc)
