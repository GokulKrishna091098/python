f=open("dd1","r")
names=set()
stopwords=[]
dict={}
for l in f:
    words=l.rstrip("\n").split(" ")

    for word in words:
        if word not in dict:
            dict[word] = 1
        else:
            dict[word] += 1
for i in dict:
    print ("word - ",i," : ",dict[i])
print(max(dict, key=dict.get))