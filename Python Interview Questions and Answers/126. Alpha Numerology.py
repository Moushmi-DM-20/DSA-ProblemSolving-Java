#Alpha Numerology

#Solution
def numer(num):
    while num>9:
        sum = 0
        while num>0:
            sum+=num%10
            num = num//10
        num = sum
    return num

def alpha(s):
    total = 0
    s = s.upper()
    for c in s:
        if 'A'<=c<='Z':
            value = (ord(c)-ord('A'))%9+1
            total += value
    return numer(total)
    
s = input("Enter : ")
# n = int(input("Enter a number : "))
print(alpha(s))
