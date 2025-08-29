#Count the elements of an array

#Solution

#Without In-Built Function
def getCount(arr):
    count = 0;
    for i in arr:
        count += 1
    return count

inputArr = list(map(int, input("Enter number with spaces : ").split()))
print("Count : ",getCount(inputArr))

#Using In-Built Function
inputArr = list(map(int, input("Enter number with spaces : ").split()))
print("Count : ",len(inputArr))
