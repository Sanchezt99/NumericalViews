import math


class Secant:
    def __init__(self):
        self.values = []

    def evaluate(self, tol, x0, x1, fun, niter, type_error=1):



        if fx0 == 0:
            return f"{x0} is the root"
        else:
            fx1 = fun.evaluate(x1)
            cont = 0
            self.values.append([-1, str(x0), str("{:.2e}".format(fx0)), None])
            self.values.append(
                [cont, str(x1), str("{:.2e}".format(fx1)), None])
            error = tol + 1
            den = fx1 - fx0

            while error > tol and fx1 != 0 and den != 0 and cont < niter:
                x2 = x1 - (fx1*(x1 - x0)/den)

                if type_error == 0:
                    error = abs(x2-x1)
                else:
                    error = abs((x2-x1)/x2)

                x0 = x1
                fx0 = fx1
                x1 = x2
                fx1 = fun.evaluate(x2)
                den = fx1 - fx0

                cont = cont + 1
                self.values.append(
                    [cont, str(x2), str("{:.2e}".format(fx1)), str("{:.2e}".format(error))])

        if fx1 == 0:
            return f"{x1} is the root"
        elif error < tol:
            return f"{x1} is an approximation to a root with a tolerance = {tol}"
        elif den == 0:
            return f"There is a possible multiple root"
        else:
            return f"Failed after {niter} iterations"

    def tabla_values(self):
        return self.values