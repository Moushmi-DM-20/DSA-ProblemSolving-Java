#Palindrome String

#Solution

#Using reverse technique - 1
inputStr= input("Enter a string : ").lower()
result = inputStr[::-1]
if inputStr==result:
    print("Palindrome")
else :
    print("Not a Palindrome")

#Using reverse technique - 2
inputStr= input("Enter a string : ").lower()
result = ''.join(reversed(inputStr))
if inputStr==result:
    print("Palindrome")
else :
    print("Not a Palindrome")

#Witout using reverse method
def palindrome(s):
    left, right = 0, len(s)-1
    while(left<=right):
        if s[left]==s[right]:
            left+=1
            right-=1
        else:
            return False
    return True
    
inputStr= input("Enter a string : ").lower()
if palindrome(inputStr):
    print("Palindrome")
else :
    print("Not a Palindrome")
