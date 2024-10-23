class Determinant:
    def calculate(matrix):
        # Recursive determinant calculation for square matrices
        if len(matrix) != len(matrix[0]):
            raise ValueError("Matrix must be square")

        # Base case for 2x2 matrix
        if len(matrix) == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

        # Recursive case for larger matrices
        det = 0
        for c in range(len(matrix)):
            det += ((-1) ** c) * matrix[0][c] * Determinant.calculate([row[:c] + row[c+1:] for row in matrix[1:]])
        return det
