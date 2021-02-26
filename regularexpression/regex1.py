import re
ctr=0
pattern="abcd"
matcher=re.finditer(pattern,"abcdacacabcdabdsabcd")
for i in matcher:
    print ("at ",i.start()," position ",i.group()," matched")
    ctr+=1
print ("Total ",pattern," -",ctr)
print("=============================================")
ctr=0
pattern="[abcd]"
matcher=re.finditer(pattern,"abcdacacabcdabdsabcd")
for i in matcher:
    print ("at ",i.start()," position ",i.group()," matched")
    ctr+=1
print ("Total ",pattern," -",ctr)
print("=============================================")
ctr=0
pattern="[a-z]"
matcher=re.finditer(pattern,"abcd 10 ABAB")
for i in matcher:
    print ("at ",i.start()," position ",i.group()," matched")
    ctr+=1
print ("Total ",pattern," -",ctr)
print("=============================================")
ctr=0
pattern="[a-zA-Z]"
matcher=re.finditer(pattern,"abcd 10 ABAB")
for i in matcher:
    print ("at ",i.start()," position ",i.group()," matched")
    ctr+=1
print ("Total ",pattern," -",ctr)
print("=============================================")
ctr=0
pattern="[0-9]"
matcher=re.finditer(pattern,"123456780")
for i in matcher:
    print ("at ",i.start()," position ",i.group()," matched")
    ctr+=1
print ("Total ",pattern," -",ctr)
print("=============================================")
ctr=0
pattern="[a-zA-Z0-9]"
matcher=re.finditer(pattern,"abAB_908%")
for i in matcher:
    print ("at ",i.start()," position ",i.group()," matched")
    ctr+=1
print ("Total ",pattern," -",ctr)
print("=============================================")
ctr=0
pattern="a+"
matcher=re.finditer(pattern,"aaaaabAaaaaB_908%")
for i in matcher:
    print ("at ",i.start()," position ",i.group()," matched")
    ctr+=1
print ("Total ",pattern," -",ctr)
print("=============================================")
ctr=0
pattern="a*"
matcher=re.finditer(pattern,"aaaaabbaaaaaaaaaab78@")
for i in matcher:
    print ("at ",i.start()," position ",i.group()," matched")
    ctr+=1
print ("Total ",pattern," -",ctr)
print("=============================================")
ctr=0
pattern="a{2}"
matcher=re.finditer(pattern,"ababAB_908%")
for i in matcher:
    print ("at ",i.start()," position ",i.group()," matched")
    ctr+=1
print ("Total ",pattern," -",ctr)
print("=============================================")
ctr=0
pattern="a{2,3}"
matcher=re.finditer(pattern,"aaaajaakjnidjas87y6")
for i in matcher:
    print ("at ",i.start()," position ",i.group()," matched")
    ctr+=1
print ("Total ",pattern," -",ctr)