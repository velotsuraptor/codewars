def determinant(matrix):
    if len(matrix)==1:
        return matrix[0]
    elif len(matrix) == 2:
        return matrix[0][0]*matrix[0][1]-matrix[1][0]*matrix[1][1]



print(determinant([[2,4,2],[3,1,1],[1,2,0]]))