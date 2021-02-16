l1=[1,3,2,4,5]
l2=[6,2,3,1,2]
l1=sorted(l1)
l2=sorted(l2)
pos1=0
pos2=0
ctr=0
while(pos1<len(l1) and pos2<len(l2) ):
    ctr+=1
    if(l1[pos1]==l2[pos2]):
        print(l1[pos1])
        pos1+=1
        pos2+=1
    elif(l1[pos1]>l2[pos2]):
        pos2+=1
    else:
        pos1+=1
print ("iteration count :",ctr)