#Write a python program to print the odd numbers in an array

#Solution

#Using Lambda function
inputArr= list(map(int,input("Enter numbers with spaces : ").split()))
result = list(filter(lambda x : x%2!=0,inputArr))
print(result)

#Without lambda function
def getOdd(arr):
    result = []
    for i in arr:
        if i%2!=0:
            result.append(i)
    return result
    
inputArr= list(map(int,input("Enter numbers with spaces : ").split()))
print(getOdd(inputArr))
