num1=input("Enter 1st number :")
num2=input("Enter 2st number :")
num3=input("Enter 3rd number :")
if (num1 > num2) & (num1 > num3):
    largest = num1
    if(num2>num3):
        largest2 = num2
    else:
        largest2 = num3
elif (num2 > num1) & (num2 > num3):
    largest = num2
    if (num1 > num3):
        largest2 = num1
    else:
        largest2 = num3
else:
    largest = num3
    if (num1 > num2):
        largest2 = num1
    else:
        largest2 = num2

print("The largest number is", largest)
print("The Second largest number is", largest2)