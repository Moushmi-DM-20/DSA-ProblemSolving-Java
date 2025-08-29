#Find the occurence of characters in a string

#Solution
def getOccurence(s):
    s = s.lower()
    count = {}
    for c in s:
        if c!=" ":
            count[c] = count.get(c,0)+1
    return count
    
inputStr = input("Enter a word : ")
result = getOccurence(inputStr)
for c,count in result.items():
    print(f"{c}:{count}")
