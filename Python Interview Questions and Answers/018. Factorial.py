#Factorial

#Solution

#Using In-Built
import math
    
num = int(input("Enter a number : "))
print(math.factorial(num))

#Using Recursion
def fact(num):
    if num<=1:
        return 1
    return num*fact(num-1)
    
num = int(input("Enter a number : "))
print(fact(num))

#Using loop
def fact(num):
    result = 1
    for i in range(1,num+1):
        result *= i
    return result
    
num = int(input("Enter a number : "))
print(fact(num))
