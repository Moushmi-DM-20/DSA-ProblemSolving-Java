#Find the largest of an array

#Solution

#Without In-Built function
def getMax(arr):
    max = arr[0]
    for i in arr:
        if i>max:
            max=i
    return max

inputVal = list(map(int, input("Enter number with spaces : ").split()))
print("Maximum = ",getMax(inputVal))

#Using In-Built Function
inputArr = list(map(int, input("Enter number with spaces : ").split()))
print("Maximum : ",max(inputArr))
