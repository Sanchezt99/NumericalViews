import java.util.Scanner;

public final class BusquedaInc {

    float initial, increment, iteration;
    double funcion;

    public BusquedaInc(Scanner s) {
        leerXanterior(s);
        leerincrement(s);
        leerIteration(s);
        
        runSearch();
    }

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        BusquedaInc BI = new BusquedaInc(s);
    }

    public double evaluateFunction(float x) {
        //funcion = 2*x;  //Write function here, input value is X
        funcion = -0.5+Math.log(Math.pow(Math.sin(x),2)+1);
        //funcion = 2.0*Math.pow(Math.sin(x)*Math.sin(x),(-1))*Math.sin(x)*Math.cos(x);
        //funcion = -x-0.5+Math.log(Math.sin(x)*Math.sin(x)+1);
        //funcion = -0.5+Math.log(Math.sin(x)*Math.sin(x)+1);
        //funcion = Math.exp(x)-x-1;
        //funcion = Math.exp(x)-1;
        funcion = Math.exp(x);
        return funcion;
    }

    public void runSearch() {
        boolean negativo = false;
        boolean positivo = false;
        boolean raiz = false;
    
        for(float i=initial; i<(initial+iteration*increment); i+=increment){
            double value1 = evaluateFunction(i);
            double value2 = evaluateFunction(i+increment);
            System.out.println(i+"value1 ="+value1+" y x2="+(i+increment)+", valor 2= "+value2);
            if(value1==0.0){ 
                System.out.println(i+" is a root");
            } else {
              if (value1*value2<0){
                System.out.println("There is a root of f in ["+i+" , "+(i+increment)+"]");
                raiz=true;
            }
        }
        }
        if(raiz == false)
        {
            System.out.println("No interval with root found");
        }
    }
    
    public void leerXanterior(Scanner s){
        System.out.println("Insert Initial Value:");
        try {
            initial = Float.parseFloat(s.next());
        } catch (NumberFormatException e) {
            System.out.println("Please enter a number");
            leerXanterior(s);
        }
    }
    
    public void leerincrement(Scanner s){
        System.out.println("Insert number of iterations:");
        try {
            iteration = Float.parseFloat(s.next());
        } catch (NumberFormatException e) {
            System.out.println("Please enter a number");
            leerincrement(s);
        }
    }
    
    public void leerIteration(Scanner s){
        System.out.println("Insert increment value:");
        try {
            increment = Float.parseFloat(s.next());
        } catch (NumberFormatException e) {
            System.out.println("Please enter a number");
            leerIteracion(s);
        }
    }
}
