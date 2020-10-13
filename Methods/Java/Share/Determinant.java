package Share;

import Errors.NoDimensionMatrix;
import Errors.NotSquareMatrix;

public class Determinant {


    /**
     * @param matrix matrix
     * @return matrix determinant
     */
    public static double determinant(double[][] matrix) throws NullPointerException, NoDimensionMatrix, NotSquareMatrix {
        if (matrix == null) throw new NullPointerException();
        if (matrix.length == 0) throw new NoDimensionMatrix("Matrix dimension 0");
        if (matrix.length != matrix[0].length) throw new NotSquareMatrix("Matrix must be a N x N dimension matrix");

        return getDeterminant(matrix);
    }

    private static double getDeterminant(double[][] matrix) {

        double determinant = 0.0;

        // returns the matrix element if dimensions are 1 x 1
        if (matrix.length == 1) return matrix[0][0];

        int sign = 1;

        for (int col = 0; col < matrix.length; ++col) {

            double[][] subMatrix = getSubMatrix(matrix, col);
            determinant = determinant + sign * matrix[0][col] * getDeterminant(subMatrix);
            sign *= -1;
        }

        return determinant;
    }

    /**
     * @param matrix parent matrix
     * @param delCol columns to be removed from parent matrix
     * @return sub matrix R-1 x C-1
     */
    private static double[][] getSubMatrix(double[][] matrix, int delCol) {
        int subMatrixDimension = matrix.length - 1;
        double[][] subMatrix = new double[subMatrixDimension][subMatrixDimension];
        int subMatrixCol = 0;
        for (int i = 0; i <= subMatrixDimension; ++i) {
            if (i != delCol) {
                for (int j = 1; j <= subMatrixDimension; ++j)
                    subMatrix[j - 1][subMatrixCol] = matrix[j][i];
                ++subMatrixCol;
            }
        }
        return subMatrix;
    }
}
