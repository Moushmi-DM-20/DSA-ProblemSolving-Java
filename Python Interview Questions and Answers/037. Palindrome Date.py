#Palindrome Date

#Solution

#Without zeros
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

#With zeros
def splitDate(date):
    day=month=year = 0
    resDate = []
    c = ""
    count = 0
    for i in date:
        if i!="/":
            c+=i
        else:
            if count==0:
                day = c
                if int(day)<10:
                    day = '0'+day
                    resDate.append(day)
            elif count==1:
                month = c
                if int(month)<10:
                    month = '0'+month
                    resDate.append(month)
            c=""
            count+=1
    year = c
    if int(year)<1000:
        year = '0'+year
        resDate.append(year)
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
