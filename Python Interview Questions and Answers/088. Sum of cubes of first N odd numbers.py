# Sum of cubes of first N odd numbers

#Solution
import math
def odd(n):
    return (i for i in range(n+1) if i%2!=0)
def sum(n):
    sum = 0
    for i in odd(n):
        sum+=math.pow(i,3)
    return sum
inputVal = int(input("Enter a number : "))
print(sum(inputVal))
