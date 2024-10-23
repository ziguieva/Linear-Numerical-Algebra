import numpy as np

class SVD:
    def compute(matrix):
        # Compute the Singular Value Decomposition using numpy
        U, S, Vt = np.linalg.svd(matrix)
        return U, S, Vt
