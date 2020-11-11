import sympy as sp
from sympy import *

x=[]
y=[]
n=0

n=int(input("Enter the number of data to use: "))
for i in range(n):
    xi=float(input("Enter the value of Xi "))
    x.append(xi)
    yi=float(input("Enter the value of Yi "))
    y.append(yi)
L=0
xx = symbols('x')


for i in range(len(x)):    
    l=1    
    for j in range(len(y)):
        if i!=j :
            l=l*((xx-x[j])/(x[i]-x[j]))
    #print(j,"|",l)
    ll = expand(l)
    print('Lagrange interpolating polynomials: ')
    print("L"+str(i), ll)
    
    for i in range(len(x)): 
           print(str(y[i])+" L"+str(i)+" ",end='')
