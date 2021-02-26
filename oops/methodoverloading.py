class Stud:
    def name(self):
        print("First name")
    def name(self,a):
        print("Second name")
    def name(self,a,b):
        print("third name")
o=Stud()
o.name(20,30)

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(self.age)
    def __str__(self):
        return self.name
obj1=Person("sukesh",30)
print(obj1)


class Stud():
    def __init__(self,name,course,marks):
        self.name=name
        self.course=course
        self.marks=marks

stud=[]

obj1=Stud("ram","mca",220)
obj2=Stud("Shyama","btech",240)
obj3=Stud("Shyam kumar","btech",180)
obj4=Stud("Shyam","bca",245)
obj5=Stud("john","mca",230)


stud.append(obj1)
stud.append(obj2)
stud.append(obj3)
stud.append(obj4)
stud.append(obj5)
print(stud)
m=[]
for student in stud:
    m.append(student.marks)
print(m)
maxx=max(m)
for student in stud:
    if student.marks==maxx:
        print(student.name)
s=[obj1,obj2,obj3,obj4,obj5]
UC=list(map(lambda stud:stud.name.upper(),s))
print(UC)
UM=list(map(lambda stud:stud.marks + 50,s))
print (UM)
MCA=list(map(lambda st:st.name,list(filter(lambda stud:stud.course=="mca",s))))
print (MCA)
max_marks=max(list(map(lambda st:st.marks,s)))
print(max_marks)