#Pattern Equation

#Solution 1
num = int(input("Enter a single digit number : "))
t1 = num
t2 = num*111
t3 = num*11111
t4 = num*1111111
T = t1+t2+t3+t4
print(f"{t1}+{t2}+{t3}+{t4}={T}")

#Solution 2
num = int(input("Enter a single digit number : "))
term = int(input("Enter number of terms : "))
total = 0
current = num
exp = ""
for i in range(term):
    digit = num*i
    current = current*11+digit
    total += current
    exp += str(current)
    if i<term-1:
        exp += '+'
print(f"{exp}+={total}")
