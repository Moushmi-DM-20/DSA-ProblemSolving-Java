#Co-Prime

#Solution

#Co-Prime Check
def coPrime(n1,n2):
    result = getGcd(n1,n2)
    if len(result)!=1:
        return False
    for i in result:
        if i!=1:
            return False
    return True
    
def getGcd(n1,n2):
    n1 = factors(n1)
    n2 = factors(n2)
    result =[]
    for i in n1:
        if i in n2:
            result.append(i)
    return result
    
def factors(n):
    result = []
    for i in range(1,n):
        if n%i==0:
            result.append(i)
    return result
    
num1 = int(input("Enter a number : "))
num2 = int(input("Enter a number : "))
if coPrime(num1,num2):
    print("Co-Prime")
else:
    print("Not a Co-Prime")

#Print Co-Prime between particular interval
def coPrime(n1,n2):
    result = getGcd(n1,n2)
    if result!=1:
        return False
    return True
    
def getGcd(n1,n2):
    if n2==0:
        return n1
    return getGcd(n2,n1%n2)
    
num = int(input("Enter a start range : "))
for i in range(1,num+1):
    if coPrime(i,num):
        print(f"The number {i} and {num} are Co-Prime")
    else:
        print(f"The number {i} and {num} are Not a Co-Prime")
