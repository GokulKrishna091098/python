num=int(input("Enter the lower limit"))
num1=int(input("Enter the Upper limit"))
flag=0
for i in range(num,num1):
    for j in range(2,num):
      if(num % i==0):
        flag=1
        break
      else:
        pass
      if(flag==0):
        print(num,"is prime")
      else:
        print(num,"is not prime")
