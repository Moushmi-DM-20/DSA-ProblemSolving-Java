#Write a program to interchange middle elements if the count of the array is even

#Solution
def interChange(arr):
    count = len(arr)
    mid1 = count//2-1
    mid2 = count//2
    arr[mid1],arr[mid2] = arr[mid2],arr[mid1]
    return arr
    
def even(arr):
    count = len(arr)
    if count%2==0:
        interChange(arr)
    return arr

inputArr = list(map(int, input("Enter number with spaces : ").split()))
print(even(inputArr))
