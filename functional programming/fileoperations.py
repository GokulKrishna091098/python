class Employee:
    def __init__(self,id,name,desig,exp,salary):
        self.id=id
        self.name=name
        self.desig=desig
        self.exp=exp
        self.salary=salary
    def __str__(self):
        return self.name
f=open("employees","r")
emplist=[]
for lines in f:
    id,name,desig,exp,salary=lines.rstrip('\n').split(",")
    emplist.append(Employee(id,name,desig,exp,salary))
dev=list(filter(lambda emp:emp.desig=="developer",emplist))
for emp in dev:
    print(emp.name)
names=list(map(lambda emp:emp.name,emplist))
print(names)