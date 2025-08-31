#Multiply without * operator

#Solution
def multiply(a,b):
    result = 0
    neg = False
    if a<0:
        a = -a
        neg = not neg
    if b<0:
        b = -b
        neg = not neg
    for i in range(b):
        result += a
    return -result if neg else result

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
print(multiply(a,b))
