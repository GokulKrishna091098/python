#n+nn+nnn......
num=int(input("Enter the num"))
sum=0
tot=0
for i in range(1,num+1):
    sum=sum * 10+ num
    tot=tot+sum

print(tot)