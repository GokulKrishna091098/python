l=[2,3,4,5,6,7]
even=[]
odd=[]
sum=0
sum1=0
for i in l:
     if (i % 2==0):
         even.append(i)
         sum=sum+i
     else:
        odd.append(i)
        sum1=sum1+i
print ("Even list",even,"Sum is",sum)
print ("odd list",odd,"sum is",sum1)