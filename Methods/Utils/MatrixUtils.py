def swapRows(matrix, row1, row2):
    temp         = matrix[row2]
    matrix[row2] = matrix[row1]
    matrix[row1] = temp

def swapValues(array, index1, index2):
        temp          = array[index1]
        array[index1] = array[index2]
        array[index2] = temp


def swapCols(matrix, col1, col2):
    for i in range(len(matrix)):
        matrix[i][col1], matrix[i][col2] = matrix[i][col2], matrix[i][col1]