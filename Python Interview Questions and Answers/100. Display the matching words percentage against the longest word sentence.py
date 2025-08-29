#Write a python program to display the matching words percentage against the longest word sentence

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
    
def checkPer(s1,s2):
    str1 = sSplit(s1)
    str2 = sSplit(s2)
    data = unCommom(s1,s2)
    count = 0
    for w, c in data.items():
        if c>1:
            count += 1
    maxCount = 0
    if len(str1)>len(str2):
        maxCount = len(str1)
    else : 
        maxCount = len(str2)
    return (count/maxCount)*100
    
fInput = input("Enter a string : ")
sInput = input("Enter a string : ")
print(f"{checkPer(fInput,sInput):.2f}%")
