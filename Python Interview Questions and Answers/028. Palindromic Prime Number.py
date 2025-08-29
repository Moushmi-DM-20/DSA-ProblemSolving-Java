#Palindromic Prime Number

#Solution
import math
def palindrome(n):
    n = list(str(n))
    left, right = 0,len(n)-1
    while left<=right:
        if n[left]==n[right]:
            left+=1
            right-=1
        else:
            return False
    return True
    
def prime(n):
    if n<2:
        return False
    sqrtn = int(math.sqrt(n))
    for i in range(2,sqrtn+1):
        if n%i!=0:
            return False
    return True
    
num = int(input("Enter a number : "))
if prime(num) and palindrome(num):
    print("Palindromic Prime")
else:
    print("Not a Palindromic Prime")
