#Decimal to binary conversion

#Solution
def binary(num):
    value = ""
    while num>0:
        value = str(num%2)+value
        num = num//2
    return value
    
num = int(input("Enter : "))
print(binary(num))
