#Check power of a number

#Solution
def power(num,base):
    if num<=0:
        return False
    while num%base==0:
        num = num//base
    return num==1
        
n = int(input("Enter a number : "))
base = int(input("Enter a number : "))
print(power(n,base))
