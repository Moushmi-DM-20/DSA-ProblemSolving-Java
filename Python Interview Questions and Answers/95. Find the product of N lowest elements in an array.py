#Write a python program to find the product of lowest elements in an array

#Solution

#Using sort Function
def findNMin(arr,n):
    A1 = arr[:]
    A1.sort()
    return A1[:n]
    
def prod(arr,n):
    A2 = findNMin(arr,n)
    result = 1
    for i in A2:
        result*=i
    return result
inputArr= list(map(int,input("Enter numbers with spaces : ").split()))
n = int(input("Enter a number : "))
print(prod(inputArr,n))

#Without sorting
def findNMin(arr,n):
    A1 = arr[:]
    result = []
    for i in range(n):
        minVal = min(A1)
        result.append(minVal)
        A1.remove(minVal)
    return result
    
def prod(arr,n):
    A2 = findNMin(arr,n)
    res = 1
    for i in A2:
        res*=i
    return res
inputArr= list(map(int,input("Enter numbers with spaces : ").split()))
n = int(input("Enter a number : "))
print(prod(inputArr,n))
