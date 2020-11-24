from math import *
    
def Bisection(limitlower,upperanger,funtion,iterations,tolerance):
   a=limitlower
   b=upperanger
   f=funtion
   i=iterations
   tol=tolerance
   control = 1

   def fun1():
        x = a
        ya = eval(f)
        return ya
    
   def fun2():
            x = b
            yb = eval(f)
            return yb
    
   def funm():
            x = c
            yc = eval(f)
            return yc

   if fun1 == 0:
        print (a,"is root")
   else:
        if fun2==0:
            print (b,"is root")
        else:
            if (fun1()*fun2())>0:
                print ("inappropriate interval")
            else:
                c = (a+b)/2
                funm()
                error = tol + 1
                cont = 1
                while (funm()!= 0)&(error>tol)&(cont<i):
                    if control == 1:
                            print ("| iter  |        a       |","      xm       |","       b       |","  f(Xm)  |","   E    |")
                            print ("|","{:5.0f}".format(cont),"|","{:14.10f}".format(a),"|","{:14.10f}".format(c),"|","{:14.10f}".format(b),"|","{:0.1e}".format(funm()),"|         |")
                            cont=cont+1
                    control=2

                    if (fun1()*funm())<0:
                            b = c
                            fun2()
    
                    else:
                            a = c
                            fun1()
    
                    xaux=c
    
                    float(c)
                    c = ((a+b)/2)
                    fm=funm()
                    float(error)
                    error = abs(c-xaux)
                    print ("|","{:5.0f}".format(cont),"|","{:14.10f}".format(a),"|","{:14.10f}".format(c),"|","{:14.10f}".format(b),"|","{:0.1e}".format(fm),"|","{:0.1e}".format(error),"|")
                    cont = cont + 1
                if funm() == 0:
                        print ("\n\n",c,"is root")
                else:
                        if error < tol:
                                print ("\n\nSe encontró una aproximación de la raiz en ","{:18.15f}".format(c))
                        else:
                                print ("failed")
                                
Bisection(0,1,'log(sin(x)**2+1)-1/2',100,0.0000001)                               
