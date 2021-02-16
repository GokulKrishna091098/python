lst=[1,2,3,4]
listnew=[]

num=int(input("Enter Number"))
low=0
upp=len(lst)-1
for i in range(0,len(lst)):
    sum=lst[low]+lst[upp]
    if(sum==num):

        listnew.append(lst[low])
        listnew.append(lst[upp])
        low+=1
    elif(sum<num):
        low+=1
    else:
        upp-=1
print(listnew)