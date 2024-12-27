class Vector:
    def __init__(self, *components):
        """
        Initialize a vector with an arbitrary number of components.
        :param components: The components of the vector, provided as individual arguments.
        """
        self.components = components

    def __repr__(self):
        """
        Provide a string representation of the vector for debugging and display.
        """
        return f"Vector{self.components}"

    def __add__(self, other):
        """
        Add two vectors component-wise.
        :param other: Another vector to add.
        :return: A new vector representing the component-wise sum.
        """
        if not isinstance(other, Vector):
            raise TypeError("Operand must be a Vector.")
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions to add.")
        return Vector(*(a + b for a, b in zip(self.components, other.components)))

    def __sub__(self, other):
        """
        Subtract another vector from this vector component-wise.
        :param other: Another vector to subtract.
        :return: A new vector representing the component-wise difference.
        """
        if not isinstance(other, Vector):
            raise TypeError("Operand must be a Vector.")
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions to subtract.")
        return Vector(*(a - b for a, b in zip(self.components, other.components)))

    def __mul__(self, scalar):
        """
        Multiply this vector by a scalar.
        :param scalar: A number to multiply each component by.
        :return: A new vector with each component multiplied by the scalar.
        """
        if not isinstance(scalar, (int, float)):
            raise TypeError("Scalar multiplication requires a number.")
        return Vector(*(a * scalar for a in self.components))

    def __rmul__(self, scalar):
        """
        Scalar multiplication from the left.
        :param scalar: A number to multiply each component by.
        :return: A new vector with each component multiplied by the scalar.
        """
        return self * scalar

    def dot(self, other):
        """
        Compute the dot product of this vector with another vector.
        :param other: Another vector.
        :return: The dot product as a scalar.
        """
        if not isinstance(other, Vector):
            raise TypeError("Operand must be a Vector.")
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions to compute the dot product.")
        return sum(a * b for a, b in zip(self.components, other.components))

    def magnitude(self):
        """
        Compute the magnitude (length) of the vector.
        :return: The magnitude as a scalar.
        """
        return sum(a ** 2 for a in self.components) ** 0.5

    def normalize(self):
        """
        Normalize the vector (make it have magnitude 1).
        :return: A new vector that is the normalized version of this vector.
        """
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize a zero vector.")
        return self * (1 / mag)

# Example usage
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
print(v1 + v2)  # Vector(5, 7, 9)
print(v1.dot(v2))  # 32
print(v1.magnitude())  # ~3.74
print(v1.normalize())  # Vector(0.267, 0.535, 0.802)