#Matrix Multiplication

#Solution
p=2
q=3
n=2
mat1 = [[int(input())for i in range(n)]for j in range(p)]
mat2 = [[int(input())for i in range(q)]for j in range(n)]
result = [[0 for i in range(q)]for j in range(p)]
for i in range(p):
    for j in range(q):
        for k in range(n):
            result[i][j] = result[i][j] + mat1[i][k]*mat2[k][j]
print(result)
