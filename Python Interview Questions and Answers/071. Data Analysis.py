#Data analysis

#Solution
def splitInt(arr):
    result =[]
    a = ""
    for i in arr:
        if i!=",":
            a+=i
        else:
            if a:
                result.append(int(a))
                a = ""
    if a:
        result.append(int(a))
    return result
    
def getSum(arr):
    A = splitInt(arr)
    sum = 0
    for i in A:
        sum+=i
    return sum
    
def getCount(arr):
    A = splitInt(arr)
    count = 0
    for i in A:
        count+=1
    return count

def getMax(arr):
    A = splitInt(arr)
    max = A[0]
    for i in A:
        if i>max:
            max = i
    return max

def getMin(arr):
    A = splitInt(arr)
    min = A[0]
    for i in A:
        if i<min:
            min = i
    return min
    
def getAvg(arr):
    sum = getSum(arr)
    count = getCount(arr)
    return sum/count
    
def getSecMax(arr):
    A = splitInt(arr)
    max = A[0]
    secondMax = A[0]
    for i in A:
        if i>max:
            secondMax = max
            max = i
        elif i<max and i>secondMax:
            secondMax = i
    return secondMax
    
inputArr = input("Enter an array with commas separated : ")
print("Sum of the array : ",getSum(inputArr))
print("Count of the array : ",getCount(inputArr))
print("Maximum of the array : ",getMax(inputArr))
print("Minimum of the array : ",getMin(inputArr))
print("Average of the array : ",getAvg(inputArr))
print("Second Maximum of the array : ",getSecMax(inputArr))
