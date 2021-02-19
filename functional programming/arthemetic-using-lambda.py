num1=(int(input("Enter First Number :")))
num2=(int(input("Enter Second Number :")))
add=lambda num1,num2:num1+num2
sub=lambda num1,num2:num1-num2
mul=lambda num1,num2:num1*num2
div=lambda num1,num2:num1/num2
mod=lambda num1,num2:num1%num2

print("SUM",add(num1,num2),"DIFFERENCE",sub(num1,num2),"PRODUCT",mul(num1,num2),"QUOTIENT",div(num1,num2),"MODULUS",mod(num1,num2))