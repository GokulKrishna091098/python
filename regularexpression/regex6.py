import re
kllist=[]
rule="[kK][lL][0-9][0-9][a-zA-z]{1,2}[0-9]{1,4}"
f=open("vehiclenumbers","r")
for i in f:
    data=i.rstrip("\n")
    match = re.fullmatch(rule, data)
    if match == None:
        pass
    else:
        kllist.append(data)

print(kllist)

fw=open("out.txt","w")
for num in kllist:
    fw.write(num+"\n")