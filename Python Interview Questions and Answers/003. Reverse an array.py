#Reverse an array

#Solution 1
arr = list(map(int,input("Enter number with spaces : ").split()))
print(arr[::-1])

#Solution 2
def reverse(arr):
    start = 0
    end = len(arr)-1
    while start<end:
        arr[start],arr[end] = arr[end],arr[start]
        start+=1
        end -=1
    return arr

arr = list(map(int,input("Enter number with spaces : ").split()))
print(reverse(arr))
