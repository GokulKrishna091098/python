class Parent:
    def add(self,name,age,wardname):
        self.name = name
        self.age = age
        self.wardname=wardname
    def print(self):
        print(self.name," ",self.age," ",self.wardname)
class Ward(Parent):
    def w1(self):
        print("inside Ward")
class Subward(Ward):
    def w2(self):
        print("Inside subward")
obj=Subward()
obj.add(name="ramesh",age="45",wardname="Ram")
obj.print()
obj.w1()
obj.w2()
