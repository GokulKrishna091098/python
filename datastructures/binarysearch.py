l=[2,7,5,4,3]
flag=0
num=int(input("Enter number to be searched"))
s=sorted(l)

low=0
high=len(l)-1
while(low<=high):
    mid=((low+high)//2)
    if(num>s[mid]):
     low=mid+1
    elif(num<s[mid]):
     high=mid-1
    elif(num==s[mid]):
     flag=1
     break
if(flag==0):
    print("Element Not Found")
else:
    print("Element  found")
