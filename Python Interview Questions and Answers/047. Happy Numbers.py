#Happy Numbers

#Solution
def happyNum(num):
    sum=0
    while num>0:
        rem = num%10
        sum+=rem*rem
        num = num//10
    if sum<10:
        return sum
    elif sum==1:
        return 1
    else:
        return happyNum(sum)

num = (int(input("Enter a number : ")))
if happyNum(num)==1:
    print("Happy Number")
else:
    print("Not a happy number")
