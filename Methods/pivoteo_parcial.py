import numpy as np
import sys
import math
# a = np.random.rand(3,3)
# b = np.random.rand(3,1)
#a = np.array([[14,3,-7,1],[6,15,4,-3],[-2,2,-23,-2],[3,-5,2,16]])
b = np.array([12,32,-24,14.0])
a = np.array([[14,6,-2,3.0],[3,15,2.0,-5],[-7,4,-23,2.],[1,-3,-2,16.0]])
b = b.reshape(4,1)
a = np.array([[2.000000, -1.000000,  0.000000,  3.000000],[1.000000,  0.500000,  3.000000,  8.000000], [0.000000,  13.000000,  -2.000000,  11.000000], [14.000000,  5.000000,  -2.000000,  3.000000]])
b = np.array([1,1,1,1])
b = b.reshape(4,1)
#a = np.array([[2,-1,0,3],[1,0.5,3,8],[0,13,-2,11],[14,5,-2,3]])



def gauss_pv(a,b):
    file1 = open("eliminacion_gaussiana_pivoteo_parcial.txt","w") 

    if a.shape[0] != a.shape[1]:
        file1.write("La matriz A debe ser cuadrada")
        file1.close()
        return 0
    
    if a.shape[1] != b.shape[0]:
        file1.write("El número de columnas de A debe ser el mismo al número de filas de b")
        file1.close()
        return 0
    
    if np.linalg.det(a) == 0:
        file1.write("El determinante de A debe ser diferente de 0")
        file1.close()
        return 0

    ns = "\n"*2
    ab = np.concatenate((a,b), axis=1)
    n,p = ab.shape
    file1.write("Eliminación Gaussiana con pivoteo parcial \n Etapa 0 \n") 
    ab = np.around(ab,6)
    file1.write(str(ab))
    file1.write(ns)    

    #ab.astype(float64)
    if ab[0,0] == 0:
        swap(ab,0,0)
    
    for etapa in range(0,n-1):
        eta = "Etapa " + str(etapa+1) + "\n"
        file1.write(eta )
        ab = swap(ab,etapa)

        for fila in range(etapa+1,n):
            if ab[fila, etapa] != 0:
                ab[fila,etapa::] = (ab[fila,etapa::] -(ab[fila, etapa]/ab[etapa,etapa] * ab[etapa,etapa::]))
        
        ab = np.around(ab,6)
        file1.write(str(ab))
        
        file1.write(ns)
        # #break
    
    print("final")
    # np.savetxt(sys.stdout, ab, fmt="%8.3f")

    x = sust_reg(ab)
    file1.write("Después de sustitución regresiva:\n x:\n")
    file1.write(str(x.T))

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


    # n = ab.shape[0]
    # maxi = -math.inf
    # maxindex=
    # for i in range(n):


    # print(f"Original matrix with etapa {etapa} \n"  )
    # np.savetxt(sys.stdout, ab, fmt="%8.3f")

    # a = np.absolute(ab)
    
    # print("finding max column of:")
    # np.savetxt(sys.stdout, a[etapa::, etapa], fmt="%8.3f")

    # maxindex = np.argmax(a[etapa::, etapa])

    # print('\n swaping rows \n')
    
    # ab[[etapa, maxindex]] = ab[[maxindex, etapa]]
    # np.savetxt(sys.stdout, ab, fmt="%8.3f")
    # print()
    # print(ab)
    return ab


def sust_reg(ab):
    n = ab.shape[0]
    
    x = np.zeros((1,n))
    x[0,n-1] = ab[n-1,n]/ab[n-1,n-1]

    for i in range(n-2,-1,-1):
        # print("\n i",i)
        aux = np.array([np.append( 1, x[0,i+1:n+1])])
        aux1 = np.array([np.append(ab[i,n],-1 * ab[i,i+1:n])]).T
        x[0,i] = np.dot(aux,aux1)/ab[i,i]

    return x
        
 

A = np.array([
    [4,3, -2, 7],
    [3,12,8,-3],
    [-14,3,-9,3],
    [1,-2,-5,6]])

# swap(A,0)
# eliminacion_gaussiana(a,b)
gauss_pv(a,b)







