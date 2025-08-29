#Write a python program to find all numbers divisible by 7 and not by 5, between 2000 and 3200

#Solution1
result = []
for i in range(2000,3201):
    if i%7==0 and i%5!=0:
        result.append(i)
print(result)

#Solution2
result = []
for i in range(2000,3201):
    if i%7==0 and i%5!=0:
        result.append(str(i))
print(','.join(result))
