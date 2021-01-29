num=int(input("Enter the num"))
flag=0
for i in range(2,num):
    if(num % i==0):
        flag=1
        break
    else:
        flag=0
if(flag==0):
    print("Prime number")
elif(flag==1):
    print("Not a prime")