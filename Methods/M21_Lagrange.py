import sympy as sp
from sympy import *



def lagrange(x,y):        
    n=len(x)
    print(n)
    xx = symbols('x')
    print("Lagrange interpolating polynomials:")
    for i in range(len(x)):    
        print(i)
        l=1    
        for j in range(len(y)):
            if i!=j :
                l=l*((xx-x[j])/(x[i]-x[j]))
        ll = expand(l)
        print("L"+str(i), ll)    
    print("Lagrange polynom")
    for i in range(len(x)): 
        print(i)
        print(str(y[i])+"*L"+str(i),end='')
        if i<len(x)-1:
             print("+",end='')
             

x=[0,1,2]
y=[4,7,10]
lagrange(x,y)
