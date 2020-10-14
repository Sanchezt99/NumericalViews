public class PuntoFijo{

    public static double g(double x){
        return Math.exp(-x);
    }

    public static double f(double x){
        return Math.exp(-x) - x;
    }

    public static void main(String[] args){
        int i = 0;
        double x = 0;
        while(Math.abs(f(x))>=1E-8 && i<=1000000) {
            x = PuntoFijo.g(x);
            i++;
        }
        if(Math.abs(f(x)) < 1E-8){
            System.out.println("Root: " + x);
        }
        else{
            System.out.println("Not possible to obtain root");
        }
    }

}