#Get user input for list

#Solution
num = (int(input("Enter a number : ")))
print(f"Enter {num} numbers")
arr = []
for i in range(num):
    data = input("Enter : ")
    arr.append(data)
print(arr)
