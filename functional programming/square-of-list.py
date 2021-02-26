lst=[2,3,4,5,6]
l=["a","abc","abcd"]
squares=list(map(lambda num:num**2,lst))
print(squares)
uc=list(map(lambda name:name.upper(),l))
print(uc)
li=[2,5,4,3,5]
cc=list(map(lambda number:number +1 if number >5 else number-1,li))
print(cc)
mk=[30,55,24,13,45]
pf=list(map(lambda mk:"p" if mk > 30 else "f",mk))
print(pf)