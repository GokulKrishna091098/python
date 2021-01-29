limit1=int(input("Enter the Lower limit"))
limit2=int(input("Enter the Upper Limit"))
for i in range(limit1,limit2+1):
    if(i % 2 ==0):
        print (i,"is even")
    else:
        print(i,"is odd")