import Utils.MatrixUtils as mu
import M8_Gauss as gs

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
    if champion != index:    
        mu.swapRows(matrix, champion, index)
        mu.swapValues(b, champion, index)


a = [   [ 2,  -1, 0, 3],
        [ 1, 0.5, 3, 8],
        [0,   13, -2, 11],
        [14,   5, -2, 3]
    ]

b = [1,1,1,1]
gauss(a,b)