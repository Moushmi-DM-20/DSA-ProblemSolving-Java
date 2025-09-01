#Matrix addition and subtraction

#Solution
def add(mat1,mat2,row,col):
    result = [[0 for i in range(col)]for j in range(row)]
    for i in range(row):
        for j in range(col):
            result[i][j] = mat1[i][j]+mat2[i][j]
    return result
    
def sub(mat1,mat2,row,col):
    result = [[0 for i in range(col)]for j in range(row)]
    for i in range(row):
        for j in range(col):
            result[i][j] = mat1[i][j]-mat2[i][j]
    return result

row = int(input("Enter the row : "))
col = int(input("Enter the column : "))
matrix1 = [[int(input()) for i in range(col)]for j in range(row)]
matrix2 = [[int(input()) for i in range(col)]for j in range(row)]
print(add(matrix1,matrix2,row,col))
print(sub(matrix1,matrix2,row,col))
