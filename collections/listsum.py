#sum of list element other than current number
#[a,b,c]
#[b+c,a+c,a+b]
list1=[2,3,4]
list2=list()
t=0
num=0
for i in list1:
    t=t+i

for j in list1:
    num=t-j
    list2.append(num)
print (list2)
