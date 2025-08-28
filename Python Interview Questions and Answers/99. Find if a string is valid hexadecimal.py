#Find if a string is a valid hexadecimal

#Solution

#Using In-Built
def checkHexa(str):
    return all(c in "0123456789ABCDEFabcdef" for c in str)
            
inputVal = input("Enter a string : ")
if checkHexa(inputVal):
    print("Hexadecimal")
else:
    print("Not Hexadecimal")

#Without In-Built
def checkHexa(str):
    for c in str:
        if not(('0'<=c<='9')or('a'<=c<='f')or('A'<=c<='F')):
            return False
    return True
            
inputVal = input("Enter a string : ")
if checkHexa(inputVal):
    print("Hexadecimal")
else:
    print("Not Hexadecimal")
