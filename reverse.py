class Reverse:
    @staticmethod
    def gauss_jordan(matrix):
        # Apply Gauss-Jordan elimination to calculate the inverse
        n = len(matrix)
        augmented = [row + identity_row for row, identity_row in zip(matrix, Inverse.identity_matrix(n))]
        
        for i in range(n):
            # Normalize the pivot row
            pivot = augmented[i][i]
            for j in range(2 * n):
                augmented[i][j] /= pivot

            # Eliminate other rows
            for k in range(n):
                if i != k:
                    factor = augmented[k][i]
                    for j in range(2 * n):
                        augmented[k][j] -= factor * augmented[i][j]

        return [row[n:] for row in augmented]

    @staticmethod
    def identity_matrix(size):
        return [[1 if i == j else 0 for j in range(size)] for i in range(size)]
