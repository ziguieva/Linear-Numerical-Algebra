from vecteur import Vector
from matrice import Matrix

def menu():
    print("Menu:")
    print("1. Vector Addition")
    print("2. Dot Product of Vectors")
    print("3. Matrix Addition")
    print("4. Matrix Transpose")
    print("5. Matrix Multiplication")
    choice = input("Select an option: ")

    if choice == "1":
        v1 = Vector([1, 2, 3])
        v2 = Vector([4, 5, 6])
        result = v1.add(v2)
        print(result)

    elif choice == "2":
        v1 = Vector([1, 2, 3])
        v2 = Vector([4, 5, 6])
        result = v1.dot_product(v2)
        print(f"Dot Product: {result}")

    elif choice == "3":
        m1 = Matrix([[1, 2], [3, 4]])
        m2 = Matrix([[5, 6], [7, 8]])
        result = m1.add(m2)
        print(result)

    elif choice == "4":
        m1 = Matrix([[1, 2], [3, 4]])
        result = m1.transpose()
        print(result)

    elif choice == "5":
        m1 = Matrix([[1, 2], [3, 4]])
        m2 = Matrix([[5, 6], [7, 8]])
        result = m1.multiply(m2)
        print(result)

if __name__ == "__main__":
    menu()
