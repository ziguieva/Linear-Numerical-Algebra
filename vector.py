# vecteur.py
class Vector:
    def __init__(self, elements):
        self.elements = elements

    def add(self, other):
        # Element-wise addition of two vectors
        return Vector([x + y for x, y in zip(self.elements, other.elements)])

    def dot_product(self, other):
        # Dot product of two vectors
        return sum(x * y for x, y in zip(self.elements, other.elements))

    def __str__(self):
        # String representation of a vector
        return f"Vector: {self.elements}"
