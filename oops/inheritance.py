class Parent:
    def add(self,name,age,wardname):
        self.name = name
        self.age = age
        self.wardname=wardname
    def print(self):
        print(self.name," ",self.age," ",self.wardname)
class Ward(Parent):
    pass
obj=Ward()
obj.add(name="ramesh",age="45",wardname="Ram")
obj.print()
