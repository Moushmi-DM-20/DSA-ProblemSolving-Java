#Linear Search

#Solution
def linear(arr,x):
    for i in range(len(arr)):
        if arr[i]==x:
            return i
    
arr = list(map(int,input("Enter number with spaces : ").split()))
target = int(input("Enter a target : "))
print(linear(arr,target))
