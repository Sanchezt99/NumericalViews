
import numpy as np
from numpy import linalg

def sor(A, b, x0, w, tol, Nmax):

    D = np.diag(np.diag(A))

    if 0 in np.diag(A):
        print("A cannot have a 0 in its diagonal")
        return 1
    
    if A.shape[0] != A.shape[1]:
        print("A must be a square matrix")
        return 1
    
    if linalg.det(A) == 0:
        print("A must be invertible")
        return 1
    




    L = -1 * np.tril(A) +D

    U = -1* np.triu(A) + D

    T = linalg.inv(D - w*L) @ ((1-w)*D + w*U)

    C = w * linalg.inv((D - w*L)) @ b

    xant = x0
    E = 1000
    cont = 0

    print()

    print("SOR \n")
    print(" iter|    E            |                         ")
    print("{:4} |                 | ".format(cont), end="")
    for i in list(x0.transpose()[0]):
            print( " {:15e} |".format(i), end="")
    print()

    while E>tol and cont < Nmax:
        xact = T @ xant + C
        E = linalg.norm(xant - xact)
        xant = xact
        cont +=1 
        a =list(xact.transpose()[0])
        print("{:4} | {:15e} | ".format(cont,E), end="")
        for i in a:
            print( " {:15e} |".format(i), end="")

        print()
        # print("{:4} | {:15e} | {:15e} | {:15e}".format(cont,E,func,error))

    

    x = xact
    iters = cont
    err = E

    # print(f"x ={x} \n with iters={iters}\n and E = {err}") 


A = np.array([
    [4,  -1   , 0,  3], 
    [1 , 15.5 , 3,  8],
    [0,  -1.3,  -4,  1.1],
    [14, 5 ,   -2,  30]])

b = np.array([1,1,1,1]).reshape(4,1)

x0 = np.array([0,0,0,0]).reshape(4,1)

tol = 10** -7

sor(A, b, x0, 1.5, tol, 100)

