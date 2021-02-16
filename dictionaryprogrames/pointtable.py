points_table={
    "england":{"pct":70.2,"points":442,"series":6,"won":11,"lost":6,"drawn":3},
    "newzealand":{"pct":70.0,"points":420,"series":5,"won":7,"lost":4,"drawn":0},
    "australia":{"pct":69.2,"points":332,"series":4,"won":8,"lost":4,"drawn":2},
    "india":{"pct":68.3,"points":430,"series":6,"won":9,"lost":4,"drawn":1}
}
c="y"
while (c=="y"):
    id=(input("Enter Country:"))
    property=(input("Enter Property:"))
    if id in points_table:
        if property in points_table[id]:
            print(property," - ",points_table[id][property])
        else:
            print("PROPERTY UNKNOWN")
    else:
        print("ID UNKNOWN")
    c=input("Do you want to continue?(y/n) :")
