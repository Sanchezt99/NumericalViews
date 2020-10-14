package Methods.Matrix;

import Errors.MatrixWithColumnZero;
import Errors.NoDimensionMatrix;
import Errors.NotSquareMatrix;
import Share.Determinant;
import Share.MatrixUtil;

public class Gauss {

    public double[] execute(double[][] matrix ,double[] b, boolean print) throws MatrixWithColumnZero, NotSquareMatrix, NoDimensionMatrix {
        Determinant.determinant(matrix);
        if (print) return gauss(matrix, b);
        return gaussNoPrint(matrix, b);
    }

    private double[] gauss(double[][] matrix ,double[] b) throws MatrixWithColumnZero {

        MatrixUtil.printAmplifiedMatrix(matrix, b);

        for (int i = 0; i < matrix.length - 1; ++i) {

            System.out.println("\u001B[31m" + "Phase " + (i+1) + "\u001B[0m");

            pivot(matrix, i, b);

            MatrixUtil.printAmplifiedMatrix(matrix, b);

            for (int j = i+1; j < matrix.length; ++j) {

                double multiplicand = matrix[j][i] / matrix[i][i];
                elimination(i, j, multiplicand, matrix, b);
            }
            MatrixUtil.printAmplifiedMatrix(matrix, b);
        }

        MatrixUtil.printAmplifiedMatrix(matrix,b);
        return linealRegression(matrix, b);
    }

    private double[] gaussNoPrint(double[][] matrix ,double[] b) throws MatrixWithColumnZero {
        for (int i = 0; i < matrix.length - 1; ++i) {
            pivot(matrix, i, b);
            for (int j = i+1; j < matrix.length; ++j) {
                double multiplicand = matrix[j][i] / matrix[i][i];
                elimination(i, j, multiplicand, matrix, b);
            }
        }
        return linealRegression(matrix, b);
    }

    void pivot(double[][] matrix, int index, double[] b) throws MatrixWithColumnZero {
        if (matrix[index][index] == 0) {
            int i = index + 1;
            while (matrix[i][index] == 0) {
                ++i;
                if (i >= matrix.length) throw new MatrixWithColumnZero("The matrix has a column full of 0");
            }
            MatrixUtil.swapRows(matrix, i, index);
            MatrixUtil.swapValues(b, i, index);
        }
    }

    void elimination(int row1, int row2, double multiplicand, double[][] matrix, double[] b) {
        for (int i = 0; i < matrix[row2].length; ++i) {
            matrix[row2][i] -= multiplicand * matrix[row1][i];
        }
        b[row2] -= multiplicand*b[row1];
    }

    double[] linealRegression(double[][] matrix, double[] b){
        double[] results = new double[matrix.length];
        int term = matrix.length -1;

        for (int i = matrix.length-1; i >= 0; --i) {
            double[] left = new double[matrix.length-i];

            for (int j = 0; j < left.length; j++) {
                left[j] = matrix[i][term-j];
            }
            results[i] = backwardSolve(left, results, b[i]);

        }
        return results;
    }

    double backwardSolve(double[] left, double[] xValues, double right) {
        if (left.length == 1) {
            return right/left[0];
        }else {
            double newRight = right - left[0]*xValues[xValues.length-1];
            return backwardSolve(MatrixUtil.frontCut(left,1), MatrixUtil.cut(xValues,1), newRight);
        }
    }

    @Override
    public String toString() {
        return "Gauss: ";
    }
}
