package Share.Functions;

import Share.Functions.IFunction;

public class TestFunction {

    public static double f(double x) {
        return Math.log(Math.pow(Math.sin(x),2) + 1) - 0.5;
    }

    public static double fPrime(double x) {
        return Math.pow(2.0*(Math.pow(Math.sin(x),2)+1), -1.0)*Math.sin(x)*Math.cos(x);
    }

    public static double fOne(double x) {
        return Math.log(Math.pow(Math.sin(x),2) + 1) - 0.5 - x;
    }

    public static double g(double x) {
        return Math.log(Math.pow(Math.sin(x),2) + 1) - 0.5;
    }

    public static double h(double x) {
        return Math.pow(Math.exp(1), x) - x - 1.0;
    }

    public static double hPrime(double x) {
        return Math.pow(Math.exp(1), x) - 1.0;
    }

    public static double hPrimeTwo(double x) {
        return Math.pow(Math.exp(1), x);
    }


    public static double[][] getA() {
        return new double[][]{
                {2, -1, 0, 3},
                {1, 0.5, 3, 8},
                {0, 13, -2, 11},
                {14, 5, -2, 3}
        };
    }

    public static double[] getB() {
        return new double[]{1,1,1,1};
    }

    // Answers{  x = 0.0384951881, y = -0.1802274716 , z = -0.3097112861 , w = 0.2475940507 }

}
