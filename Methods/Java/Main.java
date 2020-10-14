import Errors.MatrixWithColumnZero;
import Errors.NoDimensionMatrix;
import Errors.NotSquareMatrix;
import Methods.Extra.Aikten;
import Methods.Extra.Steffensen;
import Methods.Matrix.Gauss;
import Methods.Matrix.PartialPivot;
import Methods.Matrix.TotalPivot;
import Share.Functions.TestFunction;
import Share.MatrixUtil;

public class Main {

    public static void main(String[] args) {

        Gauss gauss = new Gauss();
        PartialPivot partialPivot = new PartialPivot();
        TotalPivot totalPivot = new TotalPivot();

        Gauss[] gausses = new Gauss[3];
        gausses[0] = gauss;
        gausses[1] = partialPivot;
        gausses[2] = totalPivot;

        Aikten aikten = new Aikten();
        Steffensen steffensen = new Steffensen();

        double res = steffensen.execute(x -> {
            return Math.sqrt(10.0/(x+4));
        }, 1E-7, 100, 1.5);

        double res3 = aikten.execute(x -> {
            return Math.cos(1.0/x);
        }, 1E-7, 100);

        System.out.println("Steffensen " + res);
        System.out.println("Aikten " + res3);


        try {
            for (Gauss method : gausses) {

                double[][] matrix = {
                        {2, -1, 2},
                        {1, 1, 1},
                        {-1, 4, 1}
                };

                double[] b = {4, 2, 3}; //Answers x = -0.5, y = 0, z = 2.5


                System.out.print("\u001B[31m" + method + "\u001B[0m");

                long ini = System.currentTimeMillis();
                //double[] res2 = method.execute(TestFunction.getA(), TestFunction.getB(), true);
                double[] res2 = method.execute(matrix, b, true);
                System.out.println(System.currentTimeMillis() - ini);

                MatrixUtil.printArray(res2);

            }
        } catch (Exception e) {
            e.printStackTrace();
        }

    }
}