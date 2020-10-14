import math
from scitools.StringFunction import StringFunction


def raices_multiples(f,fprima, f2prima,tol,N,x0):
    print("Raices multiples \n")
    print(" iter|      xi         |      f(xi)      |       E       ")
    
    #se inicializa los valores iniciales
    x = x0
    fun = StringFunction(f)
    func = fun(x)
    fun_prima = StringFunction(fprima)
    func_prima = fun_prima(x)
    fun_2prima = StringFunction(f2prima)
    func_2prima = fun_2prima(x)
    error = math.inf

    print("{:4} | {:15e} | {:15e} | ".format(0, x, func))
    #print(str(0).ljust(5) + "|" + str(x).ljust(22) + '|'+ str(func).ljust(22) + "|" )

    #se calcula x hasta la iteracion N o hasta que el error sea <= a tol
    for i in range(N):
        if error <= tol:
           break
        error = abs(x)
        x = x - (func * func_prima) / ( (func_prima**2) - (func * func_2prima))
        
        fun = StringFunction(f)
        func = fun(x)
        fun_prima = StringFunction(fprima)
        func_prima = fun_prima(x)
        fun_2prima = StringFunction(f2prima)
        func_2prima = fun_2prima(x)
        error = abs(error-x)

        print("{:4} | {:15e} | {:15e} | {:15e}".format(i+1,x,func,error))

        #print(str(i+1).ljust(5) + "|" + str(round(x,5)).ljust(22) + '|'+ str(round(func,5)).ljust(22) + "|" + str(round(error,5)).ljust(22) )

    
    print("\nA root approximation was found at", x)


tol = 10**-7
N = 100
funcion1 = 'pow(log(x)-1,3)'
funcion1prima = '(3* pow((log(x)-1),2))/x'
funcion12prima = '-3* (pow(log(x),2) - 4* log(x) +3)/pow(x,2)'
raices_multiples('exp(x) - x - 1','exp(x)-1' ,'exp(x)',tol,N,1)