#Sum of digits of positive integers

#Solution
def sumDigits(n):
    sum = 0
    while n>0:
        rem = n%10
        sum += rem
        n = n//10
    return sum
    
num = int(input("Enter a number : "))
print(sumDigits(num))
