import sympy as sp
import numpy as np




def hermite(x_n, y_n):

    x = sp.symbols('x')
    dimension = len(y)

    a_n = np.zeros(dimension)

    dividedDifferenceMatrix = np.zeros((dimension, dimension))

    dividedDifferenceMatrix[:, 0] = x_n
    dividedDifferenceMatrix[:, 1] = y_n

    stage = 1
    for i in range(2,dimension):    
        currentColumn = np.zeros(dimension)
        for j in range(i-1,dimension):
            currentColumn[j] = (dividedDifferenceMatrix[j][i-1] - dividedDifferenceMatrix[j-1][stage]) / (dividedDifferenceMatrix[j][0] - dividedDifferenceMatrix[j-stage][0])
        dividedDifferenceMatrix[:, i] = currentColumn
        stage += 1

    for i in range(dimension):
        a_n[i] = dividedDifferenceMatrix[i][i]

    expr = a_n[0]
    for i in range(1, dimension):
        exprn = 1
        for j in range(0,i):
            exprn *= (x-a_n[j])
        expr += exprn
    print(sp.simplify(expr))

    np.set_printoptions(formatter={'float': lambda x: "{0:0.5f}".format(x)})
    print(dividedDifferenceMatrix)


x = [0,1,2,3]
y = [1,2.71828,7.38906,20.08554]


hermite(x,y)