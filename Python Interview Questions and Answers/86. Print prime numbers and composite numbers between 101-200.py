#Print prime numbers and composite numbers between 101-200

#Solution
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
else:
    primes = []
    composites = []
    for i in range(101, inputVal+1):
        if isPrime(i):
            primes.append(i)
        else:
            composites.append(i)
    print("Prime Numbers")
    for i in primes:
        print(i)
    print("Composite Numbers")
    for i in composites:
        print(i)   
