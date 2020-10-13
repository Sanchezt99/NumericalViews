package Methods.Matrix;

import Errors.NoDimensionMatrix;
import Errors.NotSquareMatrix;
import Share.Determinant;
import Share.MatrixUtil;

public class PartialPivot extends Gauss{

    public double[] gauss(double[][] matrix ,double[] b) throws NotSquareMatrix, NoDimensionMatrix {
        Determinant.determinant(matrix);

        for (int i = 0; i < matrix.length - 1; ++i) {

            pivot(matrix, i, b);

            for (int j = i+1; j < matrix.length; ++j) {

                double multiplicand = matrix[j][i] / matrix[i][i];
                elimination(i, j, multiplicand, matrix, b);
            }
        }
        return linealRegression(matrix, b);
    }

    void pivot(double[][] matrix, int index, double[] b) {
        int champion = index;

        for (int i = index + 1; i < matrix.length; ++i)
            if (Math.abs(matrix[i][index]) > Math.abs(matrix[champion][index])) champion = i;

        MatrixUtil.swapRows(matrix, champion, index);
        MatrixUtil.swapValues(b, champion, index);
    }
}
