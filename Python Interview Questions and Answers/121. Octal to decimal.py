#Octal to decimal

#Solution
def octDecimal(s):
    deci,power = 0,0
    for i in s[::-1]:
        deci += int(i)*(8**power)
        power +=1
    return deci
    
s = input("Enter : ")
print(octDecimal(s))
