#Find the maximum subarray sum

#Solution
def maxSub(arr):
    max = arr[0]
    current = arr[0]
    for i in range(len(arr)):
        current = maxVal(arr[i],current+arr[i])
        max = maxVal(max,current)
    return max
        
def maxVal(a,b):
    if a>b:
        return a
    else:
        return b
        
arr = list(map(int,input("Enter : ").split()))
print(maxSub(arr))
