#Factorial Program

#Solution

#Using Loop
num = int(input("Enter a number : "))
product = 1;
for i in range(1,num+1):
    product *= i
print(product)

#Using In-Built function
import math
num = int(input("Enter a number : "))
print(math.factorial(num))

#Using Recursion
def fact(n):
    if n<=1:
        return 1
    return n*fact(n-1)
    
num = int(input("Enter a number : "))
print(fact(num))
