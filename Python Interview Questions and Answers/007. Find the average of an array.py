#Find the averag of an array

#Solution

#Without In-Built function
def getSum(arr):
    sum=0
    for i in arr:
        sum+=i
    return sum
    
def getCount(arr):
    count = 0
    for i in arr:
        count+=1
    return count
  
def getAvg(arr):
    sum = getSum(arr)
    count = getCount(arr)
    avg=sum/count
    return avg

inputVal = list(map(int, input("Enter number with spaces : ").split()))
print("Average = ","%.3f"%getAvg(inputVal))

#Using In-Built function
inputArr = list(map(int, input("Enter number with spaces : ").split()))
print("Average : ","%.3f"%(sum(inputArr)/len(inputArr)))
