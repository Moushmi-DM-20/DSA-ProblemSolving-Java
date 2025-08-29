#Interchange two positional elements

#Solution
def interChange(arr, ind1,ind2):
    temp = arr[ind1]
    arr[ind1] = arr[ind2]
    arr[ind2] = temp
    return arr

inputArr = list(map(int, input("Enter number with spaces : ").split()))
fElement = int(input("Enter first element : "))
sElement = int(input("Enter second element : "))
print(interChange(inputArr, fElement, sElement))
