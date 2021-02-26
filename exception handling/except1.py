no1=int(input("ENTER FIRST NUMBER :: "))
no2=int(input("ENTER SECOND NUMBER :: "))
try:
    res=no1/no2
    print(res)
except Exception as e:
    print(e.args)
print("--EXECUTION COMPLETED--")