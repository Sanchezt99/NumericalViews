
import numpy as np
from sustprog import prog_sust, reg_sust,sustitucion_regresiva
import sys
import math

def LU(A):
    n = A.shape[0]
    L = np.identity(n).astype(np.float64)
    U = np.zeros((n,n)).astype(np.float64)
    M = A
    A = A.astype(np.float64)
    P = np.identity(n).astype(np.float64)
    print(f"Etapa 0 \n")
    np.savetxt(sys.stdout, A, fmt="%8.3f")
    print()


    for etapa in range(0,n-1):
        print(f"Etapa {etapa+1} \n")
        a = np.absolute(A)
        maxindex = np.argmax(a[etapa::, etapa])
        b = a[etapa::, etapa]
        print(b)
        # if maxindex != etapa:
        A[[etapa,maxindex+etapa]] = A[[maxindex+etapa,etapa]]
        P[[etapa,maxindex+etapa]] = P[[maxindex+etapa,etapa]]
        if etapa > 0:
            aux4 = np.copy(L[etapa, 0:etapa])
            # print(f"1 {aux4}")
            L[etapa, 0:etapa] = L[etapa+maxindex, 0:etapa]
            # print(f"2 {aux4}")
            L[etapa+maxindex, 0:etapa] = aux4
            # L[etapa, 0:etapa],L[etapa+maxindex, 0:etapa] = L[etapa+maxindex, 0:etapa],L[etapa, 0:etapa]
            # print(f" second aux4 {aux4}")
        
        for fila in range(etapa+1,n):
            if A[fila, etapa] != 0:
                L[fila,etapa] = A[fila,etapa]/ A[etapa,etapa]
                multiplicador = A[fila, etapa]/A[etapa,etapa]
                A[fila,etapa::] = (A[fila,etapa::] -((A[fila, etapa]/A[etapa,etapa]) * A[etapa,etapa::]))

        print(" L: ")
        np.savetxt(sys.stdout, L, fmt="%8.3f")


        U[etapa, etapa:n+1] = A[etapa,etapa:n+1]
        U[etapa+1,etapa+1:n+1] = A[etapa+1, etapa+1:n+1]
        U[-1,-1] = A[-1,-1]

        print(" A: ")
        np.savetxt(sys.stdout, A, fmt="%8.3f")
        print(" P: ")
        np.savetxt(sys.stdout, P, fmt="%8.3f")
        print(" L: ")
        np.savetxt(sys.stdout, L, fmt="%8.3f")
        print(" U: ")
        np.savetxt(sys.stdout, U, fmt="%8.3f")


            # L[etapa, 0:etapa-1] = aux4
            
            # print("\n L: \n")
            # np.savetxt(sys.stdout, P, fmt="%8.3f")


        # print("\n original matrix")
        # np.savetxt(sys.stdout, A, fmt="%8.3f")
        # print("\n swapped matrix \n")
        # np.savetxt(sys.stdout, A, fmt="%8.3f")
        # for fila in range(etapa+1,n):



    #     U[etapa, etapa:n+1] = A[etapa,etapa:n+1]
    #     U[etapa+1,etapa+1:n+1] = A[etapa+1, etapa+1:n+1]

    #     np.savetxt(sys.stdout, A, fmt="%8.3f")
    #     print("L:")
    #     np.savetxt(sys.stdout, L, fmt="%8.3f")
    #     print("U:")
    #     np.savetxt(sys.stdout, U, fmt="%8.3f")
    #     print()
    #     # print(A)
    #     # print(U)

    # U[-1,-1] = A[-1,-1]
    # print(A)
    # print("U matrix")
    # print(U)
    # return L, U

def LU_pivpar(A,b):
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

def swap(ab,etapa):
    # print("\noriginal matrix")
    # np.savetxt(sys.stdout, ab, fmt="%8.3f")
    maxi = -math.inf
    maxindex = etapa
    n, p = ab.shape
    
    for i in range(etapa,n):
        if ab[i,etapa] > maxi:
    
            maxi = ab[i,etapa]
            maxindex= i

    ab[[etapa,maxindex]] = ab[[maxindex,etapa]]
    # np.savetxt(sys.stdout, ab, fmt="%8.3f")
    return ab

A = np.array([
    [4,3, -2, -7],
    [3,12,8,-3],
    [2,3,-9,3],
    [1,-2,-5,6]])

A2 = np.array([
    [4,-1, -10, 3],
    [1,15.5,3,8],
    [0,-1.3,-4,1.1],
    [14,5,-2, 30]])

A3 = np.array([
    [-7,2, -3, 4],
    [5,-1, 14,-1],
    [1,9,-7,5],
    [-12,13,-8, -4]])


def swap2(A,etapa):
    
    # print("swapping rows")
    a = np.absolute(A)
    maxindex = np.argmax(a[etapa::, etapa])
    # print(f"max index {maxindex+etapa} with etapa {etapa}")
    # print("searching in")
    # np.savetxt(sys.stdout, a[etapa::, etapa], fmt="%8.3f")

    A[[etapa,maxindex+etapa]] = A[[maxindex+etapa,etapa]]
    return A

b = np.array([20 ,18 , 31, 12]).transpose().reshape(4,1)

# LU_simple(A,b)
LU(A)


