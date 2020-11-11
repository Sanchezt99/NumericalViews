import numpy as np


def prog_sust(Ab):
    n = Ab.shape[0]
    x = np.zeros(n).astype(np.float64)

    x[0] = Ab[0,n]/Ab[0,0]
    

    for i in range(1,n):
        aux = np.array([np.append( 1, x[0:i].transpose())])
        aux1 = np.array([np.append(Ab[i,n],-1 * Ab[i,0:i])])
        x[i] = aux @ aux1.transpose() / Ab[i,i]
    
    return x


def reg_sust(ab):
    n = ab.shape[0]
    
    x = np.zeros((1,n))
    x[0,n-1] = ab[n-1,n]/ab[n-1,n-1]

    for i in range(n-2,-1,-1):
        aux = np.array([np.append( 1, x[0,i+1:n+1])])
        aux1 = np.array([np.append(ab[i,n],-1 * ab[i,i+1:n])]).T
        x[0,i] = np.dot(aux,aux1)/ab[i,i]

    return x
        




def sustitucion_regresiva(Ab):
    n = Ab.shape[0]
    x = np.zeros(n)
    x[n-1] = Ab[n-1][n]/float(Ab[n-1][n-1])
    for i in range(n,0,-1):
        sumatoria = 0
        for p in range(i+1,n+1):
            sumatoria += Ab[i-1][p-1]*x[p-1]
            x[i-1] = (Ab[i-1][n]-sumatoria)/float(Ab[i-1][i-1])
    return x


L = np.array([[ 1. ,         0.,          0.,          0.        ],
 [ 0.25 ,       1.,          0.,          0.        ],
 [ 0.,         -0.08253968,  1.,          0.        ],
 [ 3.5 ,        0.53968254,  0.96446701,  1.        ]])

L = np.array([[ 4 ,         3.,          -2.,          7.        ],
            [ 0. ,          .975,          9.5,       2.25     ],
            [ 0.,           0.,            9.461,      5.15        ],
            [ 0 ,           0.,            0,          7.4        ]])

L = np.array([[ 1,         0.,          0.,          0.        ],
            [ 4. ,          10,         0.,          0.        ],
            [ 6.,           8.,         9,           0         ],
            [ 9 ,           7.,         3,          1          ]])

b = np.array([9 ,10 , 20, 4]).transpose().reshape(4,1)



# sustprog(z)