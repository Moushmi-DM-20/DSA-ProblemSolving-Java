#Print the every index of duplicates in an array

#Solution
def getIndex(arr1,arr2):
    arrIndex = [i for i in range(len(arr1)) if arr1[i] in arr2]
    return arrIndex
    
def getCount(arr):
    count = {}
    for c in arr:
        if c!=" ":
            count[c] = count.get(c,0)+1
    return count
    
arr = list(map(int,input("Enter number with spaces : ").split()))
result = getCount(arr)
duplicate = []
for i,c in result.items():
    if c>=2:
        duplicate.append(i)
print(getIndex(arr,duplicate))
