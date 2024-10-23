import numpy as np

class GramSchmidt:
    def orthogonalize(vectors):
        # Apply Gram-Schmidt orthogonalization to a set of vectors
        orthogonal_vectors = []
        for v in vectors:
            for u in orthogonal_vectors:
                v -= np.dot(v, u) / np.dot(u, u) * u
            orthogonal_vectors.append(v / np.linalg.norm(v))
        return orthogonal_vectors
