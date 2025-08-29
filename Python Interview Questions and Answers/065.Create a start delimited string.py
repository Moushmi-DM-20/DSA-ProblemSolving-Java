#Create a star delimited string

#Solution

#Using In-Built
inputVal = input("Enter a string : ")
result = '*'.join(reversed(inputVal.split()))
print(result)

#Without In-Built
def wordRev(str):
    s = splitS(str)
    left,right = 0, len(s)-1
    while left<=right:
        s[left],s[right]=s[right],s[left]
        left+=1
        right-=1
    return '*'.join(s)
    
def splitS(str):
    s = []
    w = ""
    for i in str:
        if i!=" ":
            w+=i
        else:
            if w:
                s.append(w)
                w = ""
    if w:
        s.append(w)
    return s
            
inputVal = input("Enter a string : ")
print(wordRev(inputVal))
