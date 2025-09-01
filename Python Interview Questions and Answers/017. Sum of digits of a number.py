#Sum of digits of a number

#Solution
def sumDigits(num):
    sum = 0
    while num>0:
        rem = num%10
        sum += rem
        num = num//10
    return sum
    
num = int(input("Enter a number : "))
print(sumDigits(num))
