l=[3,4,6,7,8]



for i in range(0,len(l)):
    if(l[i]<5):
        l[i]=l[i]-1
    else:
        l[i]=l[i]+1
print (l)