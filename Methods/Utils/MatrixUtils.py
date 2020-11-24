import numpy as np

def swapRows(matrix, row1, row2):
    matrix[row1], matrix[row2] = np.copy(matrix[row2]), np.copy(matrix[row1])

def swapValues(array, index1, index2):
        temp          = array[index1]
        array[index1] = array[index2]
        array[index2] = temp


def swapCols(matrix, col1, col2):
    matrix[:,col1], matrix[:,col2] = np.copy(matrix[:,col2]), np.copy(matrix[:,col1]) 


def printMatrix(matrix, b):
    m = np.copy(matrix)
    cont = 0
    for i in m:
        print('[' ,end='')
        for j in i:
            print(j, " ", end= '')
        print(b[cont], " ", end= '')
        cont += 1
        print(']')