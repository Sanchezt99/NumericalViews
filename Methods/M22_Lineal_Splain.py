import numpy as np

def splain(x, y):
    dimension = 2*len(x) - 2

    matrix = np.zeros((dimension, dimension))
    m = (dimension-len(y))
    b = np.append(y, np.zeros(m))

    print(f'{len(matrix)} x {len(matrix[0])}')

    interpolation(x, matrix)
    continuity(x, matrix)

    #np.set_printoptions(formatter={'float': lambda x: "{0:0.1f}".format(x)})
    xact = np.linalg.solve(matrix, b)

    print(matrix)
    print(xact)


def interpolation(x, matrix):

    matrix[0][0] = x[0] 
    matrix[0][1] = 1

    xn = 1
    i = 0
    for j in range(1, len(x)):
        matrix[j][i]   = x[xn]
        matrix[j][i+1] = 1
        i += 2
        xn += 1

def continuity(x, matrix):
    start = len(x)
    dimension = len(matrix)


    xn = 1
    i = 0
    for j in range(start, dimension):
        matrix[j][i]   = x[xn]
        matrix[j][i+1] = 1
        matrix[j][i+2] = -x[xn]
        matrix[j][i+3] = -1
        xn += 1
        i += 2

    
x = np.array([0,1,2,3])
y = np.array([5,1,1,0])

splain(x,y)