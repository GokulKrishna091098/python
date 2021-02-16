f=open("covid_19_india.csv")
dict={}
for lines in f:
    data=lines.rstrip("\n").split(",")
    state=data[3].rstrip("***")
    if (state=="Telangana") | (state=="Telengana"):
        state="Telangana"

    confirmedcase=data[-1]
    if state not in dict:
        dict[state]=int(confirmedcase)
    else:
        dict[state]=int(confirmedcase)
print("STATE        CONFIRMED CASES")
print("-----        ---------------\n")
for i in dict:
    print(i,"\t",dict[i])
x=max(dict,key=dict.get)
y=min(dict,key=dict.get)
for j in dict:
    if j == x:
        val=dict[j]
        break
for k in dict:
    if k == y:
        val1=dict[k]
        break

print("State with maximum confirmed cases :",x," - ",val)
print("State with minimum confirmed cases :",y," - ",val1)





