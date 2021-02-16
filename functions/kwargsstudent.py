students={
    1000:{"id":1000,"name":"Ramesh","course":"Django","qualification":"Btech"},
    1001:{"id":1001,"name":"Ram","course":"Testing","qualification":"BCA"},
    1002:{"id":1002,"name":"john","course":"Django","qualification":"MCA"}
}

def getstud(**kwargs):
     id=kwargs["id"]
     if id in students:
         print(students[id]["name"])
         if prp in students[id]:
            print(students[id][prp])
         else:
             print("Property Doesn't Exist")
     else:
         print("ID ",id," Doesnt Exist")
id=(int(input("Enter ID :")))
prp=input("Enter Property :")
getstud(id=id,prp=prp)
