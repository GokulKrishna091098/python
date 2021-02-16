
def add(a,b):
    return a+b
def add(a,b,c):
    return a+b+c

print(add(20,30,40))
num=0
def f(*num):
    data=sum(num)
    return data
print (f(10,20,30))

def data(**datas):
    print(datas)
data(id=101,name="Ramesh",Jlocation="kochi",Residence="Thiruvananthapuram")
data(id=101,name="Ramesh",Jlocation="kochi",Residence="Thiruvananthapuram")