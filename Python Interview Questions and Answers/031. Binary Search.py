#Binary Search

#Solution
def binary(arr,x):
    start,end = 0,len(arr)-1
    while start<=end:
        mid = (start+end)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]<target:
            start = mid+1
        else:
            end = mid-1
    return start
    
arr = list(map(int,input("Enter number with spaces : ").split()))
target = int(input("Enter a target : "))
print(binary(arr,target))
