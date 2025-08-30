#Leap Year

#Solution

#Check leap year
num = int(input("Enter an year : "))
if (num%4==0 and num%100!=0) or num%400==0:
    print("Leap year")
else:
    print("Not a leap year")

#Print leap year between 2000-2025
for num in range(2000,2026):
    if (num%4==0 and num%100!=0) or num%400==0:
        print(num)
