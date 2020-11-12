import sympy as sp
import numpy as np




def hermite(x_n, y_n):

    x = sp.symbols('x')
    dimension = len(y)

    a_n = np.zeros(dimension)

    dividedDifferenceMatrix = np.zeros((dimension, dimension+1))

    dividedDifferenceMatrix[:, 0] = x_n
    dividedDifferenceMatrix[:, 1] = y_n

    stage = 1
    for i in range(2,dimension+1):    
        currentColumn = np.zeros(dimension)
        for j in range(i-1,dimension):
            currentColumn[j] = (dividedDifferenceMatrix[j][i-1] - dividedDifferenceMatrix[j-1][stage]) / (dividedDifferenceMatrix[j][0] - dividedDifferenceMatrix[j-stage][0])
        dividedDifferenceMatrix[:, i] = currentColumn
        stage += 1

    for i in range(dimension-1):
        a_n[i] = dividedDifferenceMatrix[i][i+1]

    print(a_n)
    expr = a_n[0]
    for i in range(1, dimension):
        exprn = a_n[i]
        for j in range(0,i):
            exprn *= (x-x_n[j])
        print(exprn)
        expr += exprn
    print(sp.simplify(expr))

    np.set_printoptions(formatter={'float': lambda x: "{0:0.5f}".format(x)})
    print(dividedDifferenceMatrix)

    print(expr.subs(x, 1))


x = [0,1,2,3]
y = [1,2.71828,7.38906,20.08554]


hermite(x,y)