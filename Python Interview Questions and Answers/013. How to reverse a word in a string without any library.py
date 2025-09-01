#How to reverse a word in a string without any library

#Solution 1
def reverseWord(s):
    result = []
    s = splitStr(s)
    for w in s:
        rw = reverse(w)
        result.append(rw)
    return ' '.join(result)
    
def reverse(s):
    s = list(s)
    start,end = 0,len(s)-1
    while start<end:
        s[start],s[end]=s[end],s[start]
        start += 1
        end -=1
    return ''.join(s)
    
def splitStr(s):
    result = []
    word = ""
    for c in s:
        if c!=" ":
            word += c
        else:
            if word:
                result.append(word)
                word = ""
    if word:
        result.append(word)
    return result
    
s = input("Enter a string : ")
print(reverseWord(s))

#Solution 2
def reverseWord(s):
    result = []
    s = splitStr(s)
    for w in s:
        rw = ''.join(list(w[::-1]))
        result.append(rw)
    return ' '.join(result)
    
def splitStr(s):
    result = []
    word = ""
    for c in s:
        if c!=" ":
            word += c
        else:
            if word:
                result.append(word)
                word = ""
    if word:
        result.append(word)
    return result
    
s = input("Enter a string : ")
print(reverseWord(s))
