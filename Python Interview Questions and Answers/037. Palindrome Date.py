#Palindrome Date

#Solution
def splitDate(date):
    resDate = []
    num = ""
    for c in date:
        if c=='/':
            resDate.append(num)
            num=""
        elif c!=" ":
            num+=c
    resDate.append(num)
    return resDate

def palindrome(date):
    result = ''.join(date)
    left,right = 0,len(result)-1
    while(left<=right):
        if result[left]==result[right]:
            left+=1
            right-=1
        else:
            return False
    return True
    
date = input("Enter day/month/year : ")
date = splitDate(date)
if palindrome(date):
    print("Palindrome Date")
else:
    print("Not a palindrome date")
