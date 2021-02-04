star="*"
num=int(input("enter number"))
for i in range(1,num):
    for j in range(1,num+4):
        if(i==num-1 or i+j==num or j-i==num-4):
            print(star,end="")
        else:
            print(" ",end="")
    print("\r")