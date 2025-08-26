// Armstrong Number Check

//Solution
def getDigitCount(n):
    r = 0
    while(n>0):
        r += 1
        n = n//10
    return r
def arms_trong(n):
    r = getDigitCount(n)
    value = 0
    while(n>0):
        rem = n%10
        value = value+pow(rem,r)
        n=n//10
    return value
output = int(input("Enter a number : "))
a = arms_trong(output)
if(a==output):
    print("Arms")
else:
    print("Not Arms")
