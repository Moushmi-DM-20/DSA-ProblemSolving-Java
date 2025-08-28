#Interchange first and last element of an array

#Solution

#Using temp
def interChange(arr):
    temp = arr[0]
    arr[0]=arr[-1]
    arr[-1] = temp
    
inputArr = list(map(int, input("Enter number with spaces : ").split()))
print(interChange(inputArr))

#Using XOR
def interChange(arr):
    arr[0]=arr[0]^arr[-1]
    arr[-1] = arr[0]^arr[-1]
    arr[0]=arr[0]^arr[-1]
    return arr
    
inputArr = list(map(int, input("Enter number with spaces : ").split()))
print(interChange(inputArr))

#Using Arithmetic Operation
def interChange(arr):
    arr[0]=arr[0]+arr[-1]
    arr[-1] = arr[0]-arr[-1]
    arr[0]=arr[0]-arr[-1]
    return arr
    
inputArr = list(map(int, input("Enter number with spaces : ").split()))
print(interChange(inputArr))

#Using len function
def interChange(arr):
    count = len(arr)
    temp=arr[0]
    arr[0] = arr[count-1]
    arr[count-1]=temp
    return arr
    
inputArr = list(map(int, input("Enter number with spaces : ").split()))
print(interChange(inputArr))
