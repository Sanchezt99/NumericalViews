package Share;

import java.util.Arrays;

public class MatrixUtil {


    public static double[][] numberMatrix(int rows, int cols, double number){
        double[][] onesMatrix = new double[rows][cols];

        for (double[] matrix : onesMatrix) {
            Arrays.fill(matrix, number);
        }

        printMatrix(onesMatrix);

        return onesMatrix;
    }

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
}
