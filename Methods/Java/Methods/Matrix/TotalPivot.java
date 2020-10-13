package Methods.Matrix;

import Errors.NoDimensionMatrix;
import Errors.NotSquareMatrix;
import Share.Determinant;
import Share.MatrixUtil;

public class TotalPivot extends PartialPivot{

    private int[] positionStamp;


    public double[] gauss(double[][] matrix ,double[] b) throws NotSquareMatrix, NoDimensionMatrix {
        Determinant.determinant(matrix);

        positionStamp = new int[matrix.length];

        for (int i = 0; i < matrix.length - 1; ++i) {

            pivot(matrix, i, b);

            for (int j = i+1; j < matrix.length; ++j) {

                double multiplicand = matrix[j][i] / matrix[i][i];
                elimination(i, j, multiplicand, matrix, b);
            }
        }

        return sort(linealRegression(matrix, b), positionStamp);
    }

    void pivot(double[][] matrix, int index, double[] b) {
        int row = index;
        int col = index;

        for (int i = row; i < matrix.length; ++i) {
            for (int j = col; j < matrix.length; ++j) {
                if (Math.abs(matrix[i][j]) > Math.abs(matrix[row][col])) {
                    row = i;
                    col = j;
                }
            }
        }
        if (col != index) {
            MatrixUtil.swapColumns(matrix, col, index);
            MatrixUtil.swapValues(positionStamp, col, index);
        }
        if (row != index) {
            MatrixUtil.swapRows(matrix, row, index);
            MatrixUtil.swapValues(b, row, index);
        }
    }

    private double[] sort(double[] values, int[] positions) {
        double[] sortedValues = new double[values.length];

        for (int i = 0; i < positions.length; ++i)
            sortedValues[positions[i]] = values[i];

        return sortedValues;
    }
}
