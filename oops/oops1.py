class Person:
    def set_values(self,name,age):
        self.name=name
        self.age=age

    def print_values(self):
        print("Name : ",self.name," Age : ",self.age )
n=(input("enter name :"))
a=(int(input("enter age:")))
obj=Person()
obj.set_values(name=n,age=a)
obj.print_values()