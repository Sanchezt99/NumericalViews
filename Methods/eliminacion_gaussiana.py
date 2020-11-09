import numpy as np

a = np.random.rand(3,3)
b = np.random.rand(3,1)
#a = np.array([[14,3,-7,1],[6,15,4,-3],[-2,2,-23,-2],[3,-5,2,16]])
b = np.array([12,32,-24,14.0])
a = np.array([[14,6,-2,3.0],[3,15,2.0,-5],[-7,4,-23,2.],[1,-3,-2,16.0]])
b = b.reshape(4,1)
a = np.array([[2.000000, -1.000000,  0.000000,  3.000000],[1.000000,  0.500000,  3.000000,  8.000000], [0.000000,  13.000000,  -2.000000,  11.000000], [14.000000,  5.000000,  -2.000000,  3.000000]])
b = np.array([1,1,1,1])
b = b.reshape(4,1)
#a = np.array([[2,-1,0,3],[1,0.5,3,8],[0,13,-2,11],[14,5,-2,3]])



def eliminacion_gaussiana(a,b):
    file1 = open("eliminacion_gaussiana.txt","w") 

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
    file1.write("Eliminación Gaussiana Simple \n Etapa 0 \n") 
    ab = np.around(ab,6)
    file1.write(str(ab))
    file1.write(ns)    

    #ab.astype(float64)
    if ab[0,0] == 0:
        swap(ab,0,0)
    
    for etapa in range(0,n-1):
        eta = "Etapa " + str(etapa+1) + "\n"
        file1.write(eta )
        if ab[etapa,etapa] == 0:
            ab = swap(ab,etapa)
        for fila in range(etapa+1,n):
            ab[fila,etapa::] = (ab[fila,etapa::] -(ab[fila, etapa]/ab[etapa,etapa] * ab[etapa,etapa::]))
        
        ab = np.around(ab,6)
        file1.write(str(ab))
        
        file1.write(ns)
        # #break
    
    x = sust_reg(ab)
    file1.write("Después de sustitución regresiva:\n x:\n")
    file1.write(str(x.T))

def swap(ab,etapa):
    n, p = ab.shape
    for i in range(etapa+1,n):
        if ab[i,etapa] != 0:
            ab[[etapa,i]] = ab[[i,etapa]]
            return ab


def sust_reg(ab):
    n = ab.shape[0]
    
    x = np.zeros((1,n))
    x[0,n-1] = ab[n-1,n]/ab[n-1,n-1]

    for i in range(n-2,-1,-1):
        print("\n i",i)
        aux = np.array([np.append( 1, x[0,i+1:n+1])])
        aux1 = np.array([np.append(ab[i,n],-1 * ab[i,i+1:n])]).T
        x[0,i] = np.dot(aux,aux1)/ab[i,i]

    return x
        
 

eliminacion_gaussiana(a,b)

