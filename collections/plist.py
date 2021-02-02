person=[101,"Ramesh","30,000","DevOps Developer"]
for i in range(0,len(person)):
    print (person[i])

salary=int(input("Enter updated salary"))
person[2]=salary

gender=input("Enter Gender")
person.append(gender)

for i in person:
    print(i)

