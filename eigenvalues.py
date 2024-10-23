import numpy as np

class Eigen:
    def power_iteration(matrix, num_iterations=100):
        # Power iteration method to calculate the dominant eigenvalue and eigenvector
        n, _ = np.shape(matrix)
        b_k = np.random.rand(n)

        for _ in range(num_iterations):
            b_k1 = np.dot(matrix, b_k)
            b_k1_norm = np.linalg.norm(b_k1)
            b_k = b_k1 / b_k1_norm

        eigenvalue = np.dot(b_k.T, np.dot(matrix, b_k)) / np.dot(b_k.T, b_k)
        return eigenvalue, b_k
