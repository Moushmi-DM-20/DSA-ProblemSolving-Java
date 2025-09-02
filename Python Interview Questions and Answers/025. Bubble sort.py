#Bubble sort

#Solution
def bubble(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr
        
num = [9,3,6,2,8,1,5]
print(bubble(num))
