#Reverse words of a string

#Solution

#Without using In-Built
def wordReverse(str):
    s = str.split(" ")
    left, right = 0,len(s)-1
    while left<=right:
        s[left],s[right] = s[right],s[left]
        left+=1
        right-=1
    return ' '.join(s)
    
inputStr= input("Enter a string : ").lower()
print(wordReverse(inputStr))

#Using In-Built function
inputStr= input("Enter a string : ").lower()
result = ' '.join(inputStr.split()[::-1])
print(result)
