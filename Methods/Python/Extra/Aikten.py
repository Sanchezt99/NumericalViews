import Error as e

def execute(f, tolerance, maxIterations):

    aikten1 = 1
    aikten2 = 0

    x  = f(1)
    x1 = f(2)
    x2 = f(3)

    i = 1
    while i <= (maxIterations and e.absoluteError(aikten1, aikten2) > tolerance):
        aikten1 = aikten2
        aikten2 = acceleration(x, x1, x2)
        x = x1
        x1 = x2
        x2 = f(i+3)
        i += 1


def acceleration(x, x1, x2):
    return x2 - ((x2 - x1)^2)/(x - 2*x1 - x2)