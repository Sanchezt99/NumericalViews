import ME1_Aikten as ak
import Utils.Error as e
import math as m


def execute(f, tolerance, maxIterations, approximation):

    x0 = f(1)
    x1 = f(2)
    x2 = f(3)
    x3 = ak.acceleration(x0, x1, x2)

    i = 1
    while i <= (maxIterations and e.absoluteError(x0, x3) > tolerance):
        x0 = x3
        x1 = f(x0)
        x2 = f(x1)
        x3 = ak.acceleration(x0, x1, x2)
        i += 1
    return x3


def fun(x):
    return m.sqrt(10/(x+4))


print(execute(fun, 1E-7, 100, 1.5))