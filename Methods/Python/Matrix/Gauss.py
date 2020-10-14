import MatrixUtils as mu
from copy import copy

def gauss(matrix, b):
    for i in range(len(matrix)):
        pivot(matrix, i, b)

        for j in range(i+1,len(matrix)):
            multiplicand = matrix[j][i] / matrix[i][i]
            elimination(i, j, multiplicand, matrix, b)
    return backwardSubstitution(matrix, b)

def pivot(matrix, index, b):
    if matrix[index][index] == 0:
        i = index + 1
        while matrix[i][index] == 0:
            i += 1
        mu.swapRows(matrix, i, index)
        mu.swapValues(b, i, index)
    
    
def elimination(row1, row2, multiplicand, matrix, b):
    for i in range(len(matrix[row2])):
        matrix[row2][i] -= multiplicand*matrix[row1][i]

    b[row2] -= multiplicand*b[row1]


def backwardSubstitution(matrix, b):
    results = [0] * len(matrix)
    term = len(matrix) - 1

    for i in range(len(matrix)-1, -1, -1):
        left = [0] * (len(matrix) - i)
        for j in range(len(left)):
            left[j] = matrix[i][term-j]
        results[i] = backwardSolve(left=left, xValues=results, right=b[i])
    return results


def backwardSolve(left, xValues, right):
    if (len(left) == 1):
        return right/left[0]
    else:
        newRight = right - left[0]*xValues[len(xValues)-1]
        newLeft = copy(left)
        newLeft.pop(0)
        newXValues = copy(xValues)
        newXValues.pop(len(xValues)-1)
        return backwardSolve(left=newLeft, xValues=newXValues, right=newRight)

