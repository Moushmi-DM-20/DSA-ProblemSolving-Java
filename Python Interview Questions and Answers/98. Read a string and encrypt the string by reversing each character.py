#Write a python program to read a string and encrypt the string by reversing each character

#Solution

#Using In-Built
inputStr= input("Enter a string : ").lower()
result = ''.join(reversed(inputStr))
print(result)

#Without using In-Built function
def wordReverse(str):
    s = str.split(" ")
    left, right = 0,len(s)-1
    while left<=right:
        s[left],s[right] = s[right],s[left]
        left+=1
        right-=1
    return s

def charReverse(str):
    s = wordReverse(str)
    result = (w[::-1] for w in s)
    return ' '.join(result)
    
inputStr= input("Enter a string : ").lower()
print(charReverse(inputStr))
