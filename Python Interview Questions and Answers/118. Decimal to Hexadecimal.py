#Decimal to Hexadecimal

#Solution
def hexa(num):
    hexaValue = "0123456789ABCDEF"
    value = ""
    if num==0:
        return 0
    while num>0:
        ind = num%16
        value = hexaValue[ind]+value
        num = num//16
    return value
    
num = int(input("Enter : "))
print(hexa(num))
