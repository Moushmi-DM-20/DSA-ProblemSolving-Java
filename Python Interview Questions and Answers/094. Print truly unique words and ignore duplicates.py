#Write a program to print truly unique words

#Solution
def getOccurence(str):
    s = str.split(" ")
    count = {}
    for w in s:
        w = w.lower()
        count[w] = count.get(w,0)+1
    return count

inputStr = input("Enter a sentence : ")
result2 = getOccurence(inputStr)
for w,count in result2.items():
    if count==1:
        print(w)
