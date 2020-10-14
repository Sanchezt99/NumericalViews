from math import *
print ("enter the lower limit of the range:")
a = float(input())
print ("enter the upper range:")
b = float(input())
print ("enter the function:")
f = input()
print ("enter the number of iterations:")
i = int(input())
print ("enter tolerance:")
tol =float(input())
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
            c = a-((fun1()*(b-a))/(fun2()-fun1()))
            funm()
            error = tol + 1
            cont = 1
            while (funm()!= 0)&(error>tol)&(cont<i):
                if (fun1()*funm())<0:
                        b = c
                        fun2()

                else:
                        a = c
                        fun1()

                xaux=c
                if control == 1:
                        print ("| iter  |        a       |","      xm       |","       b       |","     f(Xm)     |","      E        |")
                control=2

                float(c)
                c = a-((fun1()*(b-a))/(fun2()-fun1()))
                fm=funm()
                float(error)
                error = abs(c-xaux)
                print ("|","{:5.1f}".format(cont),"|","{:14.11f}".format(a),"|","{:14.11f}".format(c),"|","{:14.11f}".format(b),"|","{:14.11f}".format(fm),"|","{:14.11f}".format(error),"|")
                cont = cont + 1
            if funm() == 0:
                    print ("\n\n",c,"is root")
            else:
                    if error < tol:
                            print ("\n\n",c,"is root with tol:",error)
                    else:
                            print ("failure")
