import numpy as np


def f(x):
    return np.log(np.power(np.sin(x),2) + 1) - 0.5

def f1(x):
    return np.log(np.power(np.sin(x),2)+1)-0.5-x

def fPrime(x):
    return 2 * ( 1 / (np.power(np.sin(x), 2) + 1)) * np.sin(x) * np.cos(x)

def g(x):
    return np.log(np.power(np.sin(x),2)+1)-1/2

def h(x):
    return np.exp(x)-x-1

def hPrime(x):
    return np.exp(x) - 1

def hPrimeTwo(x):
    return np.exp(x)
