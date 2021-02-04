arr=[2,3,14,5,8]
flag=0

num=int(input("enter number to be searched :"))
for i in arr:

    if(i==num):

        flag=1
        break
    else:
        pass
if (flag==1):
    print("Element found")
else:
    print("not found")