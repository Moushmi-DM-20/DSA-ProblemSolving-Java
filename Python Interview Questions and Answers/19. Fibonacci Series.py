#Fibonacci Series

#Solution

#Recursion
def fibo(n):
    if n==0 or n==1:
        return n
    return fibo(n-1)+fibo(n-2)

def printFibo(n):
    for i in range(n):
        print(fibo(i),end=" ")
    
inputVal = int(input("Enter a number : "))
printFibo(inputVal)

#Looping
def fibo(n):
    a = 0
    b = 1
    if n==1 or n==0:
        return n
    else:
        for i in range(2,n+1):
           c=a+b
           a = b
           b = c
        return c
        
def printFibo(n):
    for i in range(n):
        print(fibo(i),end=" ")

inputVal = int(input("Enter a number : "))
printFibo(inputVal)
