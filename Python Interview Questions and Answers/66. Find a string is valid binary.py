#Find a string is valid binary

#Solution
def checkBinary(str):
    for i in str: 
        if i!='1' and i!='0':
            return False
    return True
            
inputVal = input("Enter a string : ")
if checkBinary(inputVal):
    print("Binary")
else:
    print("Not Binary")
