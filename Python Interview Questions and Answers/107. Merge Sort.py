#Merge Sort

#Solution 

#Sorted array
def merge(arr1,arr2):
    i=j=0
    result = []
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    result.extend(arr1[i:])
    result.extend(arr2[j:])
    return result

arr1 = list(map(int,input("Enter numbers with spaces : ").split()))
arr2 = list(map(int,input("Enter numbers with spaces : ").split()))
print(merge(arr1,arr2))

#Unsorted Array
def merge(arr1,arr2):
    result = arr1+arr2
    for i in range(len(result)):
        for j in range(i+1,len(result)):
            if result[i]<result[j]:
                result[i],result[j]=result[j],result[i]
    return result

arr1 = list(map(int,input("Enter numbers with spaces : ").split()))
arr2 = list(map(int,input("Enter numbers with spaces : ").split()))
print(merge(arr1,arr2))
