#Pascal's Triangle

#Solution 1
def pascal(num):
    result = [[1]]
    for i in range(num-1):
        temp = [0]+result[-1]+[0]
        tempRes = []
        for j in range(len(temp)-1):
            tempRes.append(temp[i]+temp[i+1])
        result.append(tempRes)
    return result

num = 5
print(pascal(num))

#Solution 2
import math
def pascal(num):
    for i in range(num):
        row = []
        for j in range(i+1):
            row.append(math.comb(i,j))
        print(row)
num = 5
pascal(num)
