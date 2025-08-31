#String to number

#Solution
def sToN(s):
    digitMap = {'0':0,'1':1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
    num=0
    for c in s:
        c = digitMap[c]
        num = num*10+c
    return num

str = input("Enter a number : ")
print(sToN(str))
