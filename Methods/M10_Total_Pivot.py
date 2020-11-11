import Utils.MatrixUtils as mu
import M8_Gauss as gs

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
            if abs(matrix[j][i]) > abs(matrix[row][col]):
                row = j
                col = i
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



a = [   [ 2,  -1, 0, 3],
        [ 1, 0.5, 3, 8],
        [0,   13, -2, 11],
        [14,   5, -2, 3]
    ]

b = [1,1,1,1]
gauss(a,b)