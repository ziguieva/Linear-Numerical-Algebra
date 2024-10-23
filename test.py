import unittest
from vecteur import Vector
from matrice import Matrix
from determinant import Determinant
from inverse import Inverse
from valeurs_propres import Eigen
from decomposition_svd import SVD
from orthogonalisation_gram_schmidt import GramSchmidt
from regression_lineaire import LinearRegression
import numpy as np

class TestLinearAlgebra(unittest.TestCase):
    def test_vector_addition(self):
        v1 = Vector([1, 2, 3])
        v2 = Vector([4, 5, 6])
        result = v1.add(v2)
        self.assertEqual(result.elements, [5, 7, 9])

    def test_matrix_multiplication(self):
        m1 = Matrix([[1, 2], [3, 4]])
        m2 = Matrix([[5, 6], [7, 8]])
        result = m1.multiply(m2)
        self.assertEqual(result.elements, [[19, 22], [43, 50]])

    def test_determinant(self):
        matrix = [[1, 2], [3, 4]]
        det = Determinant.calculate(matrix)
        self.assertEqual(det, -2)

    def test_matrix_inverse(self):
        matrix = [[4, 7], [2, 6]]
        inv = Inverse.gauss_jordan(matrix)
        expected = [[0.6, -0.7], [-0.2, 0.4]]
        self.assertEqual(np.allclose(inv, expected), True)

    def test_eigenvalue(self):
        matrix = [[4, 1], [2, 3]]
        eigenvalue, _ = Eigen.power_iteration(matrix)
        self.assertAlmostEqual(eigenvalue, 5.0, delta=0.1)

    def test_svd(self):
        matrix = [[1, 0], [0, 1]]
        U, S, Vt = SVD.compute(matrix)
        self.assertTrue(np.allclose(S, [1, 1]))

    def test_gram_schmidt(self):
        vectors = [np.array([3.0, 1.0]), np.array([2.0, 2.0])]
        orthogonal_vectors = GramSchmidt.orthogonalize(vectors)
        self.assertTrue(np.allclose(np.dot(orthogonal_vectors[0], orthogonal_vectors[1]), 0.0))

    def test_linear_regression(self):
        X = np.array([[1, 1], [2, 2], [3, 3]])
        y = np.array([2, 4, 6])
        model = LinearRegression()
        model.fit(X, y)
        predictions = model.predict(X)
        self.assertTrue(np.allclose(predictions, y))

if __name__ == "__main__":
    unittest.main()
