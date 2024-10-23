class Matrix:
    def __init__(self, elements):
        self.elements = elements
        self.rows = len(elements)
        self.cols = len(elements[0])

    def add(self, other):
        # Element-wise matrix addition
        return Matrix([[self.elements[i][j] + other.elements[i][j] for j in range(self.cols)] for i in range(self.rows)])

    def transpose(self):
        # Transpose of the matrix (swap rows and columns)
        return Matrix([[self.elements[j][i] for j in range(self.rows)] for i in range(self.cols)])

    def multiply(self, other):
        # Matrix multiplication (dot product between rows of the first matrix and columns of the second matrix)
        result = [[sum(self.elements[i][k] * other.elements[k][j] for k in range(self.cols)) for j in range(other.cols)] for i in range(self.rows)]
        return Matrix(result)

    def __str__(self):
        # String representation of the matrix
        return f"Matrix: {self.elements}"
