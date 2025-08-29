# Pring Nth Fibonacci number

#Solution

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

inputVal = int(input("Enter a number : "))
print(fibo(inputVal))

#Recursive
def fibo(n):
    if n==1 or n==0:
        return n
    return fibo(n-1)+fibo(n-2)

inputVal = int(input("Enter a number : "))
print(fibo(inputVal))
