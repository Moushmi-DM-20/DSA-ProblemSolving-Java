#Numerology Number

#Solution
def numer(num):
    while num>9:
        sum = 0
        while num>0:
            sum+=num%10
            num = num//10
        num = sum
    return num

    
# s = input("Enter : ")
n = int(input("Enter a number : "))
print(numer(n))
