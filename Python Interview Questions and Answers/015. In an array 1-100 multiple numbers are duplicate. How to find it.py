#In an array 1-100 multiple numbers are duplicate. How to find it

#Solution
def duplicate(arr):
    result = []
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]==arr[j]:
                if arr[i] not in result:
                    result.append(arr[i])
    return result

arr = list(map(int,input("Enter number with spaces : ").split()))
print(duplicate(arr))
