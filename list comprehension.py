l=[2,3,4,5,6]
even=[num for num in l if num%2==0]
print (even)

l1=[1,2,3]
l2=[2,3,4]
common=[num for num in l1 for num1 in l2 if num == num1 ]
print (common)

l1=[1,2,3]
l2=[4,5,6]
pairs=[(num,num1) for num in l1  for num1 in l2]
print (pairs)

l1=[[1,2],[3,4],[5,6]]
singlelist=[num1 for num in l1 for num1 in num ]
print (singlelist)

l1=[7,2,3,8,9,5]
numlessorgreater=[num-1  if num <5 else num+1 if num>5 else 5 for num in l1 ]
print (numlessorgreater)