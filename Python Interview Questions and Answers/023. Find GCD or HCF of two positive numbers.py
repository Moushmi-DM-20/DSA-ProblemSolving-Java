#Finf GCD / HCF of two positive integers

#Solution

#Using In-Built function
import math
num1 = int(input("Enter a number : "))
num2 = int(input("Enter a number : "))
print(math.gcd(num1,num2))

#Using Recursion
def getGcd(n1,n2):
    if n2==0:
        return n1
    return getGcd(n2,n1%n2)
num1 = int(input("Enter a number : "))
num2 = int(input("Enter a number : "))
print(getGcd(num1,num2))

#Without In-Built
def getDiv(n):
    result = []
    for i in range(1,n):
        if n%i==0:
            result.append(i)
    return result
    
def getMax(arr):
    max = arr[0]
    for i in arr:
        if i>max:
            max = i
    return max
    
def getGcd(n1,n2):
    n1 = getDiv(n1)
    n2 = getDiv(n2)
    result = []
    for i in n1:
        for j in n2:
            if i==j:
                result.append(i)
    gcd = getMax(result)
    return gcd
    
num1 = int(input("Enter a number : "))
num2 = int(input("Enter a number : "))
print(getGcd(num1,num2))
