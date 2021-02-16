text=(input("enter text"))
duplicates=[]
for i in text:
  if text.count(i)>1:
      if i not in duplicates:
       duplicates.append(i)
print (duplicates)