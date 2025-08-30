#Calculate LCM

#Solution

#Using loop
def getLcm(n1,n2):
    maxVal = max(n1,n2)
    while True:
        if maxVal%n1==0 and maxVal%n2==0:
            return maxVal
        maxVal+=1
        
num1 = int(input("Enter a number : "))
num2 = int(input("Enter a number : "))
print(getLcm(num1,num2))

#Using list of numbers
def getGcd(n1,n2):
    if n2==0:
        return n1
    return getGcd(n2,n1%n2)
    
def getLcm(n1,n2):
    return n1*n2//getGcd(n1,n2)
    
def listLcm(num):
    result = num[0]
    for i in num[1:]:
        result = getLcm(i,result)
    return result
        
num = list(map(int,input("Enter a number : ").split()))
print(listLcm(num))
