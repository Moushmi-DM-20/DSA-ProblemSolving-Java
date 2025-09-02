#Substring

#Solution
def subString(s):
    result = []
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            result.append(s[i:j])
    return result
        
s = "abcd"
print(subString(s))
