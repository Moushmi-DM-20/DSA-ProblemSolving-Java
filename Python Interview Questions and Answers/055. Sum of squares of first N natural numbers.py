#Sum of squares of first N natural numbers

#Solution
import math
def sum(n):
    sum = 0
    for i in range(1, n+1):
        sum+=math.pow(i,2)
    return sum
inputVal = int(input("Enter a number : "))
print(sum(inputVal))
