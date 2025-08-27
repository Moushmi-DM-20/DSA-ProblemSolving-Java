#Find the smallest number of an array

#Solution

#Without In-Built Function
def getMin(arr):
    min = arr[0]
    for i in arr:
        if i<min:
            min = i
    return min

inputVal = list(map(int, input("Enter number with spaces : ").split()))
print("Minimum = ",getMin(inputVal))

#Using In-Built Function
inputArr = list(map(int, input("Enter number with spaces : ").split()))
print("Minimum : ",min(inputArr))
