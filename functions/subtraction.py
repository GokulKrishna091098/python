#decorators
no1=int(input("enter first number:"))
no2=int(input("enter second number"))
def subupdate(fun):
    def inner(no1,no2):
        if(no1<no2):
            no1,no2=no2,no1
        return fun(no1,no2)
    return inner
@subupdate
def sub(no1,no2):
        return no1-no2
print(sub(no1,no2))