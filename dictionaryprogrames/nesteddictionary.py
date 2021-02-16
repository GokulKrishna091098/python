students={
    1000:{"id":1000,"name":"Ramesh","course":"Django","qualification":"Btech"},
    1001:{"id":1001,"name":"Ram","course":"Testing","qualification":"BCA"},
    1002:{"id":1002,"name":"john","course":"Django","qualification":"MCA"}
}
c="y"
while (c=="y"):
    id=int(input("Enter ID:"))
    property=(input("Enter Property:"))
    if id in students:
        if property in students[id]:
            print(students[id][property])
        else:
            print("PROPERTY UNKNOWN")
    else:
        print("ID UNKNOWN")
    c=input("Do you want to continue?(y/n) :")

