#Words that are greater than N

#Solution
def getWords(str,n):
    s = str.split(" ")
    result=[]
    for i in s:
        if len(i)>n:
            print(i)

inputStr= input("Enter a string : ")
num = int(input("Enter a number : "))
getWords(inputStr,num)
