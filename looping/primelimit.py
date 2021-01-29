num=int(input("Enter the lower limit"))
num1=int(input("Enter the Upper limit"))

for i in range(num,num1+1):
    for j in range(2,i):
      if(i % j==0):
        break
    else:
        print(i)
