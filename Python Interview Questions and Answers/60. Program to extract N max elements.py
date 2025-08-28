#Write a python program to extract N maximum elements

#Solution
def findNMax(arr,n):
    A1 = arr[:]
    A1.sort(reverse=True)
    return A1[:n]
    
inputArr= list(map(int,input("Enter numbers with spaces : ").split()))
n = int(input("Enter a number : "))
print(findNMax(inputArr,n))
