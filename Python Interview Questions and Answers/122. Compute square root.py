#Compute square root 

#Solution
def square(num):
    if num==0 or num==1:
        return num
    start = 0
    end = num
    ans = 0
    while start<=end:
        mid = (start+end)//2
        if mid*mid==num:
            return mid
        elif mid*mid >num:
            end = mid-1
        else:
            start = mid+1
            ans = mid
    return ans
    
num = int(input("Enter : "))
print(square(num))
