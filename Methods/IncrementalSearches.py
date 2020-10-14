from math import *
print ("enter the function:")
f = input()
print("enter the initial value (xo):")
x = float(input())
print("what is the delta:")
d = float(input())
print ("chow many maximum iterations:")
i = int(input())
#print ("minimum tolerance:")
#tol = float(input())


def func():
    res = eval(f)
    return float(res)
   
def fun1():
    x = xa
    res = eval(f)
    return res

t=log(3.14)*2
if func() == 0.0:
    print (x,"is root")
else:
    xa = x + d
    res1 = fun1()
    cont = 1 
    encontrado=False
    while (cont < i):
        x = xa
        res1 = func()
        xa = x + d
        res1 = fun1()
        cont = cont + 1
        if res1 == 0:
            print (xa,"s root")
        else:
            if (res1*func() < 0):
                print ("There is a root of f in [",x,",",xa,"]")
                encontrado=True
if ((cont==i) and (not encontrado)):
    print("With the number of requested iterations, no interval was found that could contain a root")
