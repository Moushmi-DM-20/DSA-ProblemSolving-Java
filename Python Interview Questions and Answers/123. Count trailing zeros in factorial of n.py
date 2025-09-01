#Count trailing zeros in factorial of n

#Solution
def trailZeros(num):
    count = 0
    while num>=5:
        num=num//5
        count +=num
    return count

num = int(input("Enter a number : "))
print(trailZeros(num))
