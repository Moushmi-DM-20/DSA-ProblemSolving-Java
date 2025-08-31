#Remove duplicates from an array

#Solution
def noDup(arr):
    result = []
    for i in arr:
        if i not in result:
            result.append(i)
    return result

arr = list(map(int,input("Enter numbers with spaces : ").split()))
print(noDup(arr))
