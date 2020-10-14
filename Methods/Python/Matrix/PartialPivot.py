import MatrixUtils as mu
import Gauss as gs

def gauss(matrix, b):
    for i in range(len(matrix)):
        pivot(matrix, i, b)

        for j in range(i+1,len(matrix)):
            multiplicand = matrix[j][i] / matrix[i][i]
            gs.elimination(i, j, multiplicand, matrix, b)
    return gs.backwardSubstitution(matrix, b)


def pivot(matrix, index, b):

    champion = index
    for i in range(len(matrix)):
        if abs(matrix[i][index]) > abs(matrix[champion][index]):
            champion = i
    mu.swapRows(matrix, champion, index)
    mu.swapValues(b, champion, index)


a = [   [ 2, -1, 2],
        [ 1,  1, 1],
        [-1,  4, 1]
    ]

b = [4,2,3]
print(gauss(a,b))