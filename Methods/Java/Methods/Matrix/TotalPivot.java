package Methods.Matrix;

import Errors.MatrixWithColumnZero;
import Errors.NoDimensionMatrix;
import Errors.NotSquareMatrix;
import Share.MatrixUtil;

public class TotalPivot extends PartialPivot{

    private int[] positionStamp;

    @Override
    public double[] execute(double[][] matrix, double[] b) throws NotSquareMatrix, NoDimensionMatrix, MatrixWithColumnZero {

        initPositionStamp(matrix.length);
        return sort(super.execute(matrix, b), positionStamp);
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

    private void initPositionStamp(int length) {
        if (positionStamp == null) {
            positionStamp = new int[length];
            for (int i = 0; i < length; i++) {
                positionStamp[i] = i;
            }
        }
    }

    private double[] sort(double[] values, int[] positions) {
        double[] sortedValues = new double[values.length];

        for (int i = 0; i < positions.length; ++i)
            sortedValues[positions[i]] = values[i];

        return sortedValues;
    }
}
