#Perfect Numbers

#Solution

#Check Perfect Number
def perfect(n):
    sum = 0
    for i in range(1, n):
        if n%i==0:
            sum+=i
    return sum
    
num = int(input("Enter a number : "))
if num==perfect(num):
    print("Perfect Number")
else:
    print("Not a Perfect Number")

#Print Perfect numbers between some interval
def perfect(n1,n2):
    sum = 0
    for num in range(n1,n2+1):
        sum = 0
        for i in range(1, num):
            if num%i==0:
                sum+=i
        if sum==num:
            print(num)
    
num1 = int(input("Enter a start number : "))
num2 = int(input("Enter a end number : "))
perfect(num1,num2)
