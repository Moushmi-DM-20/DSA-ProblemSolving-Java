#  Check if all digits are even

#Solution
def checkEven(num):
    while num>0:
        rem = num%10
        if rem%2!=0:
            return False
        num = num//10
    return True
    
num = int(input("Enter a number : "))
print(checkEven(num))
