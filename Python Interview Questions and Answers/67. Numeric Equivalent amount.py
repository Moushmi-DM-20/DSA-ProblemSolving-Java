Numeric Equivalent amount

#Solution
def findRes(str,num):
    result = float(str.replace(",",""))
    return result*num/100
            
inputVal = input("Enter a string : ")
num = float(input("Enter a number : "))
print(findRes(inputVal,num))
