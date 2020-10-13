package Methods.Extra;

import Share.Functions.IFunction;

public class Steffensen {

    private final Aikten aikten = new Aikten();

    public double execute(IFunction f, double tolerance, int maxIterations, double approximation) {
        double x0, x1, x2, x3;

        x0 = approximation;
        x1 = f.evaluate(x0);
        x2 = f.evaluate(x1);
        x3 = aikten.acceleration(x0, x1, x2);

        for (int i = 1; i <= maxIterations && aikten.absoluteError(x0, x3) > tolerance; ++i) {
            x0 = x3;
            x1 = f.evaluate(x0);
            x2 = f.evaluate(x1);
            x3 = aikten.acceleration(x0, x1, x2);
        }
        return x3;
    }
}
