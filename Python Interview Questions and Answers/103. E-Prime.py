#E-Prime

#Solution
def ePrime(s):
    s = splitS(s)
    toBeWords = ["is","am","are","was","were","be","been","being"]
    newSen = []
    for w in s:
        if w.lower() not in toBeWords:
            newSen.append(w)
        else:
            newSen += ""
    return ' '.join(newSen)
    
def splitS(s):
    result= []
    w = ""
    for c in s:
        if c!=" ":
            w +=c
        else:
            if c:
                result.append(w)
                w = ""
    if c:
        result.append(w)
    return result

s=input("Enter a sentence : ")
print(ePrime(s))
