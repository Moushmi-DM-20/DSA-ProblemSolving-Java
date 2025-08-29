#Reverse a string

#Solution

#Using loop
def reverseStr(s):
    s = list(s)
    left,right = 0, len(s)-1
    while left<=right:
        s[left],s[right] = s[right],s[left]
        left+=1
        right-=1
    return ''.join(s)
    
str = input("Enter a string : ")
print(reverseStr(str))

#Using In-Built
str = input("Enter a string : ")
print(''.join(reversed(str)))
