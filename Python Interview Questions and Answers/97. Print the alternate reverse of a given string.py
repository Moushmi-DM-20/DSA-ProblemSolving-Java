#Write a python program to alternate reverse of the given string

#Solution
def altReverse(str):
    s = list(str)
    n = len(s)
    for i in range(0, n-1, 2):
        s[i],s[i+1]=s[i+1],s[i]
    return ''.join(s)
    
inputStr= input("Enter a string : ").lower()
print(altReverse(inputStr))
