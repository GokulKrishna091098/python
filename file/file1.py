f=open("d1","r")
l=[]
for lines in f:
    l.append(lines.rstrip("\n"))
print(l)
