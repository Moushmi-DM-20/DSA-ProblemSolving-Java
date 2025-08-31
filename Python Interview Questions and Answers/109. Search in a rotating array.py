#Search in a roatating array

#Solution
def search(arr,t):
    left,right = 0,len(arr)-1
    while left<=right:
        mid = (left+right)//2
        if arr[mid]==t:
            return mid
        if arr[left]<=arr[mid]:
            if arr[left]<=target<arr[mid]:
                right =mid-1
            else:
                left = mid+1
        else:
            if arr[mid]<target<=arr[right]:
                left = mid+1
            else:
                right = mid-1
    return -1
    
arr = list(map(int,input("Enter numbers with spaces : ").split()))
target = int(input("Enter a number : "))
print(search(arr,target))
