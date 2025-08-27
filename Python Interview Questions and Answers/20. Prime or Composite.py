//Prime or Composite Number

//Solution
import math
def isPrime(n):
    sqrtn = int(math.sqrt(n))
    prime = True
    for i in range(2, sqrtn+1):
        if(n%i==0):
            prime = False
            break
    return prime

inputVal = int(input("Enter a number : "))
if inputVal<2:
    print("Neither prime nor composite")
elif isPrime(inputVal):
    print("Prime Number")
else:
    print("Composite Number")
