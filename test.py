# matrix multiplication
#input two 2d arrays and determine elegibility

#[[2],[1]] commas seperate lines [[1, 2]]

#len(matrix) = rows
# len(matrix[0]) = col

# Do recursively

# [[1,2],[1]]

matrix1 = [[1,2],[3,4]] # [[1],[2]] A
matrix2 = [[5,6],[7,8]] # [[2,1]] B
# A [[1]]

# [[1,2]] and [] 

def transpose_matrix(X, n):
    # switches rows with columns
    return list(map(lambda d: [d[n]],X))

def determineValidity(A,B):
    return len(A[0]) == len(B) and type(A).__name__ and type(B).__name__ == "list"

def matrix_mult(A, B):
    output_matrix = []
    if determineValidity(A,B):
        c_ij = 0
        if len(A) and len(B[0]) == 1: # only one row A and one col B
            if len(output_matrix) == 0:
                output_matrix.append([])
            for i in range(len(A[0])):
                c_ij += A[0][i] * B[i][0]
                if len(output_matrix) < i + 1:
                    output_matrix.append([])
                if len(output_matrix[i]) < i + 1:
                    output_matrix.append(c_ij)
                else:
                    output_matrix[i][i] = c_ij
        else:
            for row in range(len(A)):
                aug_A = [A[row]]
                for col in range(len(B[0])):
                    aug_B = transpose_matrix(B,col)
                    print(aug_A, aug_B)
                    print(output_matrix)
                    matrix_mult([aug_A],aug_B)
    return output_matrix

def matrix_mult2(A,B):
    pass


print(matrix_mult(matrix1, matrix2))