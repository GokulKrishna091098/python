num1=input("Enter 1st number :")
num2=input("Enter 2st number :")
num3=input("Enter 3rd number :")
if (num1 > num2) & (num1 > num3):
    largest = num1
    if(num2>num3):
        largest2 = num2
        largest3 = num3
    else:
        largest2 = num3
        largest3 = num2
elif (num2 > num1) & (num2 > num3):
    largest = num2
    if (num1 > num3):
        largest2 = num1
        largest3 = num3
    else:
        largest2 = num3
        largest3 = num1
else:
    largest = num3
    if (num1 > num2):
        largest2 = num1
        largest3 = num2

    else:
        largest2 = num2
        largest3 = num1
print("The sorted order(descending) is", largest, "" , largest2 ,"" ,largest3)
print("The sorted order(ascending) is", largest3 , "" , largest2 ,"" ,largest)
