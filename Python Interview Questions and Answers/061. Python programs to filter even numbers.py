Write a python program to filter even numbers

#Solution

#Using Lambda function
inputArr= list(map(int,input("Enter numbers with spaces : ").split()))
result = list(filter(lambda x : x%2==0 and x!=0,inputArr))
print(result)

#Without using lambda function
def getEven(arr):
    result = []
    for i in arr:
        if i%2==0 and i!=0:
            result.append(i)
    return result
    
inputArr= list(map(int,input("Enter numbers with spaces : ").split()))
print(getEven(inputArr))
