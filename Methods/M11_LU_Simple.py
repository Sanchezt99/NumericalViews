
import numpy as np
from sustprog import prog_sust, reg_sust,sustitucion_regresiva
import sys

def LU(A):
    n = A.shape[0]
    L = np.identity(n)
    U = np.zeros((n,n))
    M = A
    A = A.astype(np.float64)
    L = L.astype(np.float64)
    U = U.astype(np.float64)
    print(f"Etapa 0 \n")
    np.savetxt(sys.stdout, A, fmt="%8.3f")
    print()


    for etapa in range(0,n-1):
        print(f"Etapa {etapa+1} \n")
        if A[etapa,etapa] == 0:
            print("A connot have 0 in its diagonal")
            return 1
        for fila in range(etapa+1,n):
            if A[fila, etapa] != 0:
                L[fila,etapa] = A[fila,etapa]/ A[etapa,etapa]
                multiplicador = A[fila, etapa]/A[etapa,etapa]
                uno = (A[fila,etapa::])
                dos = A[etapa,etapa::]
                tres = ((A[fila, etapa] / A[etapa, etapa]) * A[etapa, etapa::])
                A[fila,etapa::] = (A[fila,etapa::] -((A[fila, etapa]/A[etapa,etapa]) * A[etapa,etapa::]))

        U[etapa, etapa:n+1] = A[etapa,etapa:n+1]
        U[etapa+1,etapa+1:n+1] = A[etapa+1, etapa+1:n+1]

        np.savetxt(sys.stdout, A, fmt="%8.3f")
        print("L:")
        np.savetxt(sys.stdout, L, fmt="%8.3f")
        print("U:")
        np.savetxt(sys.stdout, U, fmt="%8.3f")
        print()
        # print(A)
        # print(U)

    U[-1,-1] = A[-1,-1]
    print(A)
    print("U matrix")
    print(U)
    return L, U

def LU_simple(A,b):
    L, U = LU(A)
    lb = np.concatenate((L,b),axis=1)
    z = prog_sust(lb)
    z = z.reshape((z.shape[0],1))
    print("z")
    print(z)
    
    uz = np.concatenate((U,z), axis=1)
    print("Uz \n")
    print(uz)
    print("x")
    x = sustitucion_regresiva(uz)
    print(x)

A = np.array([
    [4,3, -2, -7],
    [3,12,8,-3],
    [2,3,-9,3],
    [1,-2,-5,6]])

# A = np.array([
#     [4,-1, 0, 3],
#     [1,15.5,3,8],
#     [0,-1.3,-4,1.1],
#     [14,5,-2, 30]])

b = np.array([20 ,18 , 31, 12]).transpose().reshape(4,1)

LU_simple(A,b)


