#Valid date

#Solution

#Getting input value in 3 line
day = int(input("Enter a day : "))
month = int(input("Enter a month : "))
year = int(input("Enter an year : "))

if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
    days = 31
elif month==4 or month==6 or month==9 or month==11:
    days = 30
elif (year%4==0 and year%100!=0) or year%400==0:
    days = 29
else:
    days = 28
    
if day<1 or day>days:
    print("Enter valid day")
elif month<1 or month>12:
    print("Enter valid month")
else:
    print("Valid date")

#Getting input in single line
day,month,year = map(int,input("Enter day/month/year : ").split('/'))

if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
    days = 31
elif month==4 or month==6 or month==9 or month==11:
    days = 30
elif (year%4==0 and year%100!=0) or year%400==0:
    days = 29
else:
    days = 28
    
if day<1 or day>days:
    print("Enter valid day")
elif month<1 or month>12:
    print("Enter valid month")
else:
    print("Valid date")

#Without In-Built
date = input("Enter day/month/year : ")
day=month=year = 0
c = ""
count = 0
for i in date:
    if i!="/":
        c+=i
    else:
        if count==0:
            day = int(c)
        elif count==1:
            month = int(c)
        c=""
        count+=1
year = int(c)

if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
    days = 31
elif month==4 or month==6 or month==9 or month==11:
    days = 30
elif (year%4==0 and year%100!=0) or year%400==0:
    days = 29
else:
    days = 28
    
if day<1 or day>days:
    print("Enter valid day")
elif month<1 or month>12:
    print("Enter valid month")
else:
    print("Valid date")
