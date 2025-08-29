#Palindrome Number check

#Solution 1
def palindrome(n):
    sum = 0
    while n>0:
        rem = n%10
        sum = sum*10+rem
        n = n//10
    return sum
    
num = int(input("Enter a number : "))
if num==palindrome(num):
    print("Palindrome")
else:
    print("Not a Palindrome")

#Solution 2
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
    
num = int(input("Enter a number : "))
if palindrome(num):
    print("Palindrome")
else:
    print("Not a Palindrome")
