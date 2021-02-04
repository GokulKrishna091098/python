lst=[[1,2,3],[4,5,6],[7,8,9]]
new=[]
for i in range(0,len(lst)):
    for j in lst[i]:
        new.append(j)
print (new)