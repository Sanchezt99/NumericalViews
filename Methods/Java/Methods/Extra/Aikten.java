package Methods.Extra;

import Share.Functions.IFunction;

public class Aikten {

    public double execute(IFunction f, double tolerance, int maxIterations) {
        double x, x1, x2;

        double aikten1 = 1;
        double aikten2 = 0;

        x  = f.evaluate(1);
        x1 = f.evaluate(2);
        x2 = f.evaluate(3);

        for (int i = 1; i <= maxIterations && absoluteError(aikten1, aikten2) > tolerance; ++i) {
            aikten1 = aikten2;
            aikten2 = acceleration(x, x1, x2);
            x = x1;
            x1 = x2;
            x2 = f.evaluate(i+3);
        }
        return aikten2;
    }

    double acceleration(double x, double x1, double x2) {
        return x2 - (Math.pow(x2-x1,2))/(x - 2*x1 + x2);
    }

    double absoluteError(double x, double x1) {
        return Math.abs(x1-x);
    }
}
