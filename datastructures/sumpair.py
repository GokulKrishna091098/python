arr=[2,3,4,5]
sum=int(input("Enter sum :"))
s=0
f=0
for i in arr:
    for j in arr:
     if(i+j==sum):
         print (i,j)
     else:
         pass
