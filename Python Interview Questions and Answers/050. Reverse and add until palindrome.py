#Reverse and add untile palindrome

#Solution
def palindrome(num):
    temp = num
    sum = 0
    while num>0:
        rem = num%10
        sum = sum*10+rem
        num = num//10
    if sum==temp:
        return sum
    else:
        num=temp+sum
        return palindrome(num)
    
num = (int(input("Enter a number : ")))
print(palindrome(num))
