#Binary to Decimal

#Solution
def biDecimal(s):
    deci,power = 0,0
    for i in s[::-1]:
        deci += int(i)*(2**power)
        power +=1
    return deci
    
s = input("Enter : ")
print(biDecimal(s))
