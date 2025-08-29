#Sum of elements in an array

#Solution

#Without using inbuilt function
def getSum(arr):
    sum=0
    for i in arr:
        sum+=i
    return sum

inputVal = list(map(int, input("Enter number with spaces : ").split()))
print("Sum = ",getSum(inputVal))

#Using In-Built function
inputArr = list(map(int, input("Enter number with spaces : ").split()))
print("Sum : ",sum(inputArr))
