package Methods.Matrix;

import Share.MatrixUtil;

public class PartialPivot extends Gauss{

    void pivot(double[][] matrix, int index, double[] b) {
        int champion = index;

        for (int i = index + 1; i < matrix.length; ++i)
            if (Math.abs(matrix[i][index]) > Math.abs(matrix[champion][index])) champion = i;

        MatrixUtil.swapRows(matrix, champion, index);
        MatrixUtil.swapValues(b, champion, index);
    }

    @Override
    public String toString() {
        return "Partial Pivot: ";
    }
}
