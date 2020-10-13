package Share;

public class Functions {

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

}
