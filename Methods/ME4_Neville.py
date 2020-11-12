import numpy as np
import sympy as sym
from sympy import *

xi = []
fi = []
b=[]


n=int(input("Enter the number of data to use: "))
for i in range(n):
    x=float(input("Enter the value of Xi "))
    xi.append(x)
    f=float(input("Enter the value of Yi "))
    fi.append(f)
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
