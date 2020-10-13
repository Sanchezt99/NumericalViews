import Methods.Matrix.Gauss;
import Methods.Matrix.PartialPivot;
import Methods.Matrix.TotalPivot;

public class Main {

    public static void main(String[] args) {

        double [][] matrix = {
                {2,-1,2},
                {1,1,1},
                {-1,4,1}
        };
        //z = 2.5 y = 0 x = -0.5 {4 2 3}

        double [][] matrix2 = {
                {2,-1,2},
                {1,1,1},
                {-1,4,1}
        };
        double [][] matrix3 = {
                {2,-1,2},
                {1,1,1},
                {-1,4,1}
        };

        double[] b = {4, 2, 3};
        double[] b2 = {4, 2, 3};
        double[] b3 = {4, 2, 3};

        Gauss gauss = new Gauss();
        PartialPivot partialPivot = new PartialPivot();
        TotalPivot totalPivot = new TotalPivot();
        try {
            /*
            long ini = System.currentTimeMillis();
            gauss.gauss(matrix, b);
            System.out.println(System.currentTimeMillis()-ini);

            ini = System.currentTimeMillis();
            partialPivot.gauss(matrix2, b2);
            System.out.println(System.currentTimeMillis()-ini);
            */

            double[] res3 = totalPivot.gauss(matrix3, b3);

            for (double v : res3) {
                System.out.println(v);
            }

        } catch (Exception e) {
            e.printStackTrace();
        }

    }





}