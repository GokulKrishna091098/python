#wordcount
text=input("Enter text :")
wordlist = text.split(" ")
dict={}

for word in wordlist:
    if word not in dict:
        dict[word]=1
    else:
        dict[word]+=1

print(max(dict, key=dict.get))