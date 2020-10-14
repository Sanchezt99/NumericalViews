import MatrixUtils as mu
import Gauss as gs

def gauss(matrix, b):
    positionStamp = [0] * len(matrix)

    for i in range(len(positionStamp)):
        positionStamp[i] = i

    for i in range(len(matrix)):
        pivot(matrix, i, b, positionStamp)

        for j in range(i+1,len(matrix)):
            multiplicand = matrix[j][i] / matrix[i][i]
            gs.elimination(i, j, multiplicand, matrix, b)
    return sort(gs.backwardSubstitution(matrix, b), positionStamp)


def pivot(matrix, index, b, positionStamp):
    row = index
    col = index

    for i in range(row, len(matrix)):
        for j in range(col, len(matrix)):
            if abs(matrix[i][j]) > abs(matrix[row][col]):
                row = i
                col = j
    if col != index:
        mu.swapCols(matrix, col, index)
        mu.swapValues(positionStamp, col, index)
    if row != index:
        mu.swapRows(matrix, row, index)
        mu.swapValues(b, row, index)

def sort(values, positions):
    sortedValues = [0] * len(values)
    for i in range(len(positions)):
        sortedValues[positions[i]] = values[i]
    return sortedValues



a = [   [ 2, -1, 2],
        [ 1,  1, 1],
        [-1,  4, 1]
    ]

b = [4,2,3]
print(gauss(a,b))