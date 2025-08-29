#Swapping numbers

#Solution

#Using third variable
def swap(n1,n2):
    temp = n1
    n1=n2
    n2=temp
    print (f"After swapping num1 : {n1} and num2 : {n2}")
    
num1 = int(input("Enter a first number : "))
num2 = int(input("Enter a second number : "))
swap(num1,num2)

#Without Third variable
num1 = int(input("Enter a first number : "))
num2 = int(input("Enter a second number : "))
num1,num2=num2,num1
print (f"After swapping num1 : {num1} and num2 : {num2}")

#Using Arithmetic operations 1
num1 = int(input("Enter a first number : "))
num2 = int(input("Enter a second number : "))
num1 = num1+num2
num2 = num1-num2
num1 = num1-num2
print (f"After swapping num1 : {num1} and num2 : {num2}")

#Using Arithmetic operations 2
num1 = int(input("Enter a first number : "))
num2 = int(input("Enter a second number : "))
num1 = num1*num2
num2 = int(num1/num2)
num1 = int(num1/num2)
print (f"After swapping num1 : {num1} and num2 : {num2}")

#Using XOR Operation
num1 = int(input("Enter a first number : "))
num2 = int(input("Enter a second number : "))
num1 = num1^num2
num2 = num1^num2
num1 = num1^num2
print (f"After swapping num1 : {num1} and num2 : {num2}")
