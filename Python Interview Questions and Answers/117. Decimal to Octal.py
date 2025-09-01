#Decimal to Octal

#Solution
def octal(num):
    value = ""
    while num>0:
        value = str(num%8)+value
        num = num//8
    return value
    
num = int(input("Enter : "))
print(octal(num))
