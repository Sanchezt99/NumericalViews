import numpy as np
import sys
import warnings
from numpy import inf

# warnings.filterwarnings('error')


def cholesky(A, b):
    n = A.shape[0]
    L = np.identity(n, dtype=complex)
    U = np.identity(n, dtype=complex)
    print(f"Shape of b: {b.shape}")

    for i in range(n):
        d = A[i, i] - np.dot(L[i, 0:i], U[0:i, i].transpose())
        c = np.sqrt(complex(d))
        L[i, i] = c

        U[i, i] = L[i, i]
        for j in range(i+1, n):
            L[j, i] = (A[j, i] - np.dot(L[j, 0:i],
                                        U[0:i, i].transpose())) / U[i, i]
            U[i, j] = (A[i, j] - np.dot(L[i, 0:i],
                                        U[0:i, j].transpose())) / L[i, i]

        print(f"Etapa {i+1} \n")
        print("L: \n")
        np.savetxt(sys.stdout, L, fmt="%8.3f")
        print("U: \n")
        np.savetxt(sys.stdout, U, fmt="%8.3f")
        print()

    L[n-1, n-1] = A[n-1, n-1] - np.dot(L[n-1, 0:n], U[0:n, n-1].transpose())
    U[n-1, n-1] = L[n-1, n-1]

    lb = np.concatenate((L, b), axis=1)
    z = prog_sust(lb)
    z = z.reshape((z.shape[0], 1))
    print("Z")
    np.savetxt(sys.stdout, z, fmt="%8.2f")

    uz = np.concatenate((U, z), axis=1)
    x = reg_sust(uz)

    # x = sustitucion_regresiva(uz)

    print("Despues de aplicar sustitución progresiva y regresiva: \n x: \n")
    np.savetxt(sys.stdout, x, fmt="%8.2f")


#
def reg_sust(ab):
    n = ab.shape[0]

    x = np.zeros((1, n), dtype=complex)
    x[0, n - 1] = ab[n - 1, n] / ab[n - 1, n - 1]

    for i in range(n - 2, -1, -1):
        aux = np.array([np.append(1, x[0, i + 1:n + 1])])
        aux1 = np.array([np.append(ab[i, n], -1 * ab[i, i + 1:n])]).T
        x[0, i] = np.dot(aux, aux1) / ab[i, i]

    return x


def prog_sust(Ab):
    n = Ab.shape[0]
    np.savetxt(sys.stdout, Ab, fmt="%8.3f")
    print(Ab)
    x = np.zeros(n, dtype=complex)

    x[0] = Ab[0, n]/Ab[0, 0]

    for i in range(1, n):
        aux = np.array([np.append(1, x[0:i].transpose())])
        aux1 = np.array([np.append(Ab[i, n], -1 * Ab[i, 0:i])])
        x[i] = aux @ aux1.transpose() / Ab[i, i]
        #(1,2) * (2,1)
    return x


A = np.array([
    [36, 3, -4, 5],
    [5, -45, 10, -2],
    [6, 8, 57, 5],
    [2, 3, -8, -42]
])

A = np.array([[4, -1, 0, 3],
              [1, 15.5, 3, 8],
              [0, -1.3, -4, 1.1],
              [14, 5, -2, 30]
              ])
b = np.array([1, 1, 1, 1]).reshape(4, 1)

cholesky(A, b)
