import numpy as np
import sys
from sustprog import prog_sust, reg_sust,sustitucion_regresiva


def crout(A,b):
    n = A.shape[0]
    L = np.identity(n, dtype=np.float64)
    U = np.identity(n, dtype=np.float64)
    print(f"Shape of b: {b.shape}")

    for i in range(n):
        for j in range(i,n):
            L[j,i] = A[j,i] - np.dot(L[j,0:i], U[0:i,i].transpose())
        for j in range(i+1,n):
            U[i,j] = (A[i,j] - np.dot(L[i, 0:i], U[0:i, j].transpose())) / L[i,i]
        
        print(f"Etapa {i+1} \n")
        print("L: \n")
        np.savetxt(sys.stdout, L, fmt="%8.3f")
        print("U: \n")
        np.savetxt(sys.stdout, U, fmt="%8.3f")
        print()
        
    
    L[n-1,n-1] = A[n-1,n-1]  - np.dot(L[n-1,0:n], U[0:n,n-1].transpose())

    lb = np.concatenate((L,b),axis=1)

    n = lb.shape[0]
    z = prog_sust(lb)

    z = z.reshape((z.shape[0],1))
    
    
    uz = np.concatenate((U,z), axis=1)

    x = reg_sust(uz).transpose()

    print("Despues de aplicar sustitución progresiva y regresiva: \n x: \n")
    np.savetxt(sys.stdout, x, fmt="%8.2f")



A = np.array([[4, -1, 0 ,3],
        [1, 15.5, 3, 8],
        [0, -1.3, -4, 1.1],
        [14, 5, -2, 30]
        ])
b = np.array([1,1,1,1]).reshape(4,1)

crout(A,b)