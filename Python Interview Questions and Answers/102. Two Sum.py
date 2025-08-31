#Two Sum

#Solution
arr=list(map(int,input("Enter number with spaces : ").split()))
target = int(input("Enter a target : "))
for i in arr:
    for j in range(i,len(arr)-1):
        if i+arr[j]==target:
            print(f"The numbers are {i} and {arr[j]}")
