import Utils.MatrixUtils as mu
import numpy as np
import M8_Gauss as gs

def gauss(matrix, b):
    for i in range(len(matrix)):
        pivot(matrix, i, b)

        for j in range(i+1,len(matrix)):
            multiplicand = matrix[j][i] / matrix[i][i]
            gs.elimination(i, j, multiplicand, matrix, b)
    return gs.backwardSubstitution(matrix, b)


def pivot(matrix, index, b):

    relativeValues = len(matrix) - index

    champion = index
    championValue = 0
    for i in range(relativeValues):
        maxRowValue = np.max(np.absolute(matrix[index + i]))
        maxRowRelativeValue = matrix[index + i][index]/maxRowValue
        if championValue < maxRowRelativeValue:
            champion = index + i
            championValue = maxRowRelativeValue
    
    if champion != index:
        mu.swapRows(matrix, champion, index)
        mu.swapValues(b, champion, index)

a = np.array([  [ 2, 3,  0],
                [-1, 2, -1],
                [ 3, 0,  2]
            ])

b = [8,0,9]
print(gauss(a,b))