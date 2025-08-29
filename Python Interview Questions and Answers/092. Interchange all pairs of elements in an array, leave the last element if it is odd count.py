#Write a program to interchange all pairs of elements, Leave the last element if the count is odd

#Solution
def interChange(arr):
    count = len(arr)
    for i in range(0, count-1,2):
        arr[i],arr[i+1] = arr[i+1],arr[i]
    return arr

inputArr = list(map(int, input("Enter number with spaces : ").split()))
print(interChange(inputArr))
