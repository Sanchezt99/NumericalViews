package Share;

public class MatrixUtil {

    public static double[] frontCut(double[] array, int cut) {
        double[] newArray = new double[array.length-cut];

        if (newArray.length >= 0) System.arraycopy(array, cut, newArray, 0, newArray.length);
        return newArray;
    }

    public static double[] cut(double[] array, int cut) {
        double[] newArray = new double[array.length-cut];

        if (newArray.length >= 0) System.arraycopy(array, 0, newArray, 0, newArray.length);
        return newArray;
    }

    public static void swapRows(double[][] matrix, int row1, int row2) {
        double[] temp = matrix[row2];
        matrix[row2]  = matrix[row1];
        matrix[row1]  = temp;
    }

    public static void swapValues(double[] array, int index1, int index2){
        double temp   = array[index1];
        array[index1] = array[index2];
        array[index2] = temp;
    }

    public static void swapValues(int[] array, int index1, int index2){
        int temp   = array[index1];
        array[index1] = array[index2];
        array[index2] = temp;
    }

    public static void  swapColumns(double[][] matrix, int col1, int col2){
        for (int i = 0; i < matrix.length; ++i) {
            double temp = matrix[i][col1];
            matrix[i][col1] = matrix[i][col2];
            matrix[i][col2] = temp;
        }
    }

    public static void printMatrix(double[][] matrix){
        for (double[] doubles : matrix) {
            System.out.print("{");
            for (int i = 0; i < doubles.length; ++i) {
                if ((i + 1) == doubles.length) System.out.println(doubles[i] + "}");
                else System.out.print(doubles[i] + ", ");
            }
        }
        System.out.println();
    }

    public static void printArray(double[] array) {
        System.out.print("{");
        for (int i = 0; i < array.length; ++i) {
            if (i + 1 < array.length) System.out.print(array[i]+ ", ");
            else System.out.print(array[i]);
        }
        System.out.println("}");
    }

    public static double[][] amplifyMatrix(double[][] matrix, double[] array) {
        double[][] amplifiedMatrix = new double[matrix.length][matrix.length + 1];
        for (int i = 0; i < matrix.length; ++i) {
            System.arraycopy(matrix[i], 0, amplifiedMatrix[i], 0, matrix.length);
            amplifiedMatrix[i][matrix.length] = array[i];
        }
        return amplifiedMatrix;
    }

    public static void printAmplifiedMatrix(double[][] matrix, double[] array) {
        printMatrix(amplifyMatrix(matrix, array));
    }
}
