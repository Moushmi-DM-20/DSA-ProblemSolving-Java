#Find the unique words and the occurence of words in a string

#Solution
def getOccurence(str):
    s = str.split(" ")
    count = {}
    for w in s:
        w = w.lower()
        count[w] = count.get(w,0)+1
    return count

def getUnique(str):
    s = str.split(" ")
    result = []
    for w in s:
        w =w.lower()
        if w not in result:
            result.append(w)
    return result

inputStr = input("Enter a sentence : ")
print("Unique Words")
print(getUnique(inputStr))
print("Occurance of Words")
result2 = getOccurence(inputStr)
for w,count in result2.items():
    print(f"{w} : {count}")
