#Write a python program to extract N maximum elements

#Solution

#Using sorting
def findNMax(arr,n):
    A1 = arr[:]
    A1.sort(reverse=True)
    return A1[:n]
    
inputArr= list(map(int,input("Enter numbers with spaces : ").split()))
n = int(input("Enter a number : "))
print(findNMax(inputArr,n))

#Without Sorting
def findNMax(arr,n):
    A1 = arr[:]
    result = []
    for i in range(n):
        maxVal = max(A1)
        result.append(maxVal)
        A1.remove(maxVal)
    return result
    
inputArr= list(map(int,input("Enter numbers with spaces : ").split()))
n = int(input("Enter a number : "))
print(findNMax(inputArr,n))
