#Transpose of a matrix

#Solution
def Transpose(mat,row,col):
    result = [[0 for i in range(row)]for j in range(col)]
    for i in range(col):
        for j in range(row):
            result[i][j] = mat[j][i]
    return result


row = int(input("Enter the row : "))
col = int(input("Enter the column : "))
matrix = [[int(input()) for i in range(col)]for j in range(row)]
print(Transpose(matrix,row,col))
