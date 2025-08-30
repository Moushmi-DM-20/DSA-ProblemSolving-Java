#Calculate LCM using GCD

#Solution

def getGcd(n1,n2):
    if n2==0:
        return n1
    return getGcd(n2,n1%n2)
    
def getLcm(n1,n2):
    return n1*n2//getGcd(n1,n2)
        
num1 = int(input("Enter a number : "))
num2 = int(input("Enter a number : "))
print(getLcm(num1,num2))
