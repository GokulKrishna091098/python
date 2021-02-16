f=open("dd1","r")
names=set()
stopwords=['the','where','is','have','with','that','and','were','been','had','of','a','to']

dict={}
for l in f:
    words=l.rstrip("\n").rstrip(",").split(" ")

    for word in words:
        if word in stopwords:
            pass
        elif word not in dict:
            dict[word] = 1
        else:
            dict[word] += 1
for i in dict:
    print ("word - ",i," : ",dict[i])
print(max(dict, key=dict.get))