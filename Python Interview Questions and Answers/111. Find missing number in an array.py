#Find missing number in an array

#Solution
def missing(arr):
    missing =-1
    for i in range(1,len(arr)+1):
        if i not in arr:
            missing = i
    return missing
arr = list(map(int,input("Enter : ").split()))
print(missing(arr))
