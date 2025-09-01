#Find longest word of a given sentence

#Solution
def longString(s):
    s = splitStr(s)
    maxStr = s[0]
    for i in s:
        if len(s)>len(maxStr):
            maxStr = s
    return maxStr
    
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
print(longString(s))
