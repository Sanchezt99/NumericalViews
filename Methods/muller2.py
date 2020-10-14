import math
from decimal import *

from scitools.StringFunction import StringFunction


def muller(f,x0,x1,x2,tol,N):
    x=0
    e = math.inf
    fun = StringFunction(f)
    print("Muller method")
    print(" iter|      x0         |        x1        |      x2          |          Root     |          E           ")

    h1 = x1 - x0
    h2 = x2 - x1
    t1 = (fun(x1) - fun(x0))/h1
    t2 = (fun(x2) - fun(x1))/h2
    d = (t2 - t1)/ (h2 + h1)

    print("{:4} | {:15e} | {:15e}  | {:15e}  |                   |                    ".format(0, x0, x1,x2))
    for i in range(3,N):
        b = t2 + h2*d
        D = (b**2 - 4*fun(x2)*d)**(1/2)

        if abs(b-D) < abs(b+D):
            E = b+D
        else:
            E = b - D
        
        h = (-2*fun(x2))/E
        if i != 3:
            e = x

        x = x2 + h

        if i != 3:
            e = abs(e-x)

        if i != 3:
            print("{:4} | {:15e} | {:15e}  | {:15e}  |  {:15e}  | {:15e} ".format(i-2, x0, x1,x2,x,e))

        if i == 3:
            print("{:4} | {:15e} | {:15e}  | {:15e}  |  {:15e}  | ".format(i-2, x0, x1,x2,x))


        if abs(e) <= tol:
            print("A root aproximation was found at",x)
            break

        x0 = x1
        x1 = x2
        x2 = x
        h1 = x1 - x0
        h2 = x2 - x1
        t1 = (fun(x1) - fun(x0))/h1
        t2 = (fun(x2) - fun(x1))/h2
        d = (t2 - t1)/ (h2 + h1)

tol = 10**-2
N=100
f = '(pow(sin(x),2) + 1) - (1/2)'
f1 = 'pow(2*x,2)-1'
muller('exp(x) - x - 1',-1,0,1,tol,N)