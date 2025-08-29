#Find unique words in a string

#Solution

#In sentence
def getUniqueWords(str):
    s = str.split(" ")
    result = []
    for w in s:
        if w not in result:
            result.append(w)
    return result

inputStr = input("Enter a sentence : ")
finalResult = getUniqueWords(inputStr)
print(" ".join(finalResult))

#In list
def getUniqueWords(str):
    s = str.split(" ")
    result = []
    for w in s:
        if w not in result:
            result.append(w)
    return result

inputStr = input("Enter a sentence : ")
print(getUniqueWords(inputStr))
