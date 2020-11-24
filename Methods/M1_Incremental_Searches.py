
from math import *


def Incrementalsearches(function,initialvalue,delta,iterations):
   f=function
   xo=initialvalue     
   d=delta
   i=iterations

   def func():
       x=xo
       res = eval(f)
       return float(res)
      
   def fun1():
       x=xa
       res = eval(f)
       return res

   if func() == 0.0:
       print (x,"is root")
   else:
       cont = 1 
       encontrado=False
       while (cont < i):
           res1 = func()
           xa = xo + d
           res2 = fun1()
           if res2 == 0:
               print (xa,"is root")
           else:
               if (res1*res2 < 0):
                   print ("There is a root of f in [","{:14.10f}".format(xo),",","{:14.10f}".format(xa),"]")
                   encontrado=True
           cont = cont + 1
           xo=xa
   if ((cont==i) and (not encontrado)):
       print("With the number of requested iterations, no interval was found that could contain a root")

Incrementalsearches('log(sin(x)**2+1)-1/2', -3, 0.5, 100)

