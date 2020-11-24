import numpy as np
import sympy as sym
from sympy import *

def neville(xi,fi):
    b=[]
    n=len(xi)
    for i in range(n):
        b.append(0)
    xx = symbols('x')
    xi=np.array(xi)
    fi=np.array(fi)
    
    n = xi.size
    q =[]
    
    for i in range(n):
        q.append([])
        for j in range(n):
            q[i].append(None)
    
    for i in range(n):
        q[i][0]=fi[i]
            
    
    
    for i in range(1, n):
        for j in range(1, i + 1):
            q[i][j]= ((xx - xi[i - j]) * q[i][ j - 1] - (xx - xi[i]) * q[i - 1][ j - 1]) / (xi[i] - xi[i - j])
            
    print(q)
    
    pol = q[n - 1][ n - 1]
    pol = expand(pol)
    pol = simplify(pol)    
    print(pol)

x=[0,1,2]
y=[4,7,10]
neville(x,y)
