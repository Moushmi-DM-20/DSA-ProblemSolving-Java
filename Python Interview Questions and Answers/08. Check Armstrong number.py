// Armstrong Number Check

//Solution
def getCount(n):
    count = 0
    while(n>0):
        count+= 1
        n = n//10
    return count
    
def armStrong(num):
    count = getCount(num)
    orgVal = num
    value = 0
    while(num>0):
        rem = num%10
        value += pow(rem, count)
        num = num//10
    return value
    
inputVal = int(input("Enter a number : "))
outputVal = armStrong(inputVal)
if(inputVal == outputVal):
    print("This is Armstrong")
else:
    print("This is not Armstrong")
