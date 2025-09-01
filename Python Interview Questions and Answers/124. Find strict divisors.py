#Find strict divisors

#Solution
def strictDivisors(num):
    divisors = []
    for i in range(1,num):
        if num%i==0:
            divisors.append(i)
    return divisors

num = int(input("Enter a number : "))
print(strictDivisors(num))
