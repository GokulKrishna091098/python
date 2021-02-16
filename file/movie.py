f=open("movies.csv")
dict={}
for lines in f:
    data=lines.rstrip("\n").split(",")
    year=data[2]
    if year not in dict:
        dict[year]=1
    else:
        dict[year]+=1
print(dict)
print("Year with maximum movie release - ",max(dict,key=dict.get))