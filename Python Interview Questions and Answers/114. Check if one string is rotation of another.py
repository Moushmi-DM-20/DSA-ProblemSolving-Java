#Check if one string is rotation of another

#Solution
def checkStrRotation(s1,s2):
    if len(s1)!=len(s2):
        return False
    return s2 in (s1+s1)
    
s1 = input("Enter : ")
s2 = input("Enter : ")
print(checkStrRotation(s1,s2))
