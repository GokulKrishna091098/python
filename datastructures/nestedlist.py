employees=[[101,"raj","Developer",50000,1970,1999],[102,"rajini","Developer",40000,1980,1989],[103,"john","QA Manager",45000,1998,2005]]
sum=0
i=1
salary=[]
for emp in employees:
    if emp[2]=="Developer":
        print (emp)
    else:
        pass
for emp in employees:
    print("Salary ",i," :", emp[3])
    sum=sum+emp[3]
    i+=1
print("------------------")
print("Total      :",sum)
for emp in employees:
    salary.append(emp[3])
print (salary)
print(max(salary))


maxsal=max(list(map(lambda emp:emp[3],employees)))
print(maxsal)


from _functools import reduce
sumsal=reduce(lambda sal1,sal2 :sal1+sal2,list(map(lambda emp:emp[3],employees)))
print (sumsal)

for emp in employees:
    if(emp[5]>=1990):
        print(emp)
exp=0
experience=[]

for emp in employees:
    exp=emp[5]-emp[4]
    experience.append(exp)
print (experience)
for emp in employees:
    x=emp[5] - emp[4]
    if(max(experience)==x):
        print (emp[1],"",x,"years")

