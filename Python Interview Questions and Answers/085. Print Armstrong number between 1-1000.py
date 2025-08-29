//Pring Armstrong number between 1-1000

//Solution
def getCount(n):
    count = 0
    while(n>0):
        count+= 1
        n = n//10
    return count
    
def armStrong(num):
    count = getCount(num)
    value = 0
    while(num>0):
        rem = num%10
        value += pow(rem, count)
        num = num//10
    return value

inputVal = int(input("Enter a number : "))
for i in range(inputVal):
    if(i == armStrong(i)):
        print(i)
