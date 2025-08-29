#Write a python program to find all numbers between 1000 and 3000 such that each digits of the number is even

#Solution
def evenDigits(num):
    temp = num
    while(num>0):
        rem = num%10
        if rem%2!=0:
           return False
        num = num//10
    return True
    
result = []
for i in range(1000,3001):
    if evenDigits(i):
        result.append(i)
print(result)
