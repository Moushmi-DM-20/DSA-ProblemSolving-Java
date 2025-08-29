#Find uncommon words from two strings

#Solution
def sSplit(s):
    result = []
    w = ""
    for x in s:
        if x!=" ":
            w += x
        else:
            if w:
                result.append(w)
                w = ""
    if w:
        result.append(w)
    return result
    
def unCommom(s1,s2):
    str1 = sSplit(s1)
    str2 = sSplit(s2)
    count = {}
    for w in str1+str2:
        w = w.lower()
        count[w] = count.get(w,0)+1
    return count
    
fInput = input("Enter a string : ")
sInput = input("Enter a string : ")
result = unCommom(fInput,sInput)
output = []
for w, count in result.items():
    if count==1:
        output.append(w)
print(output)
