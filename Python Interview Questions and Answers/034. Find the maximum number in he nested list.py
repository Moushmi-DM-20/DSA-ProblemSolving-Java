#Find the maximum number in the nested list

#Solution
def arrList(arr):
    for i in arr:
        if type(i)==list:
            arrList(i)
        else:
            result.append(i)
    return result
    
def getMax(arr):
    arr = arrList(arr)
    max = arr[0]
    for i in arr:
        if i>max:
            max = i
    return max
    
arr = [2,6,[8,3],4,3]
result = []
print(getMax(arr))
