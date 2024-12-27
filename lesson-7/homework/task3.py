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

    def __mul__(self, other):
        """
        Perform dot product if the operand is a vector, or scalar multiplication if it is a number.
        :param other: A vector for dot product or a scalar for multiplication.
        :return: Dot product as a scalar or a new scaled vector.
        """
        if isinstance(other, Vector):
            if len(self.components) != len(other.components):
                raise ValueError("Vectors must have the same dimensions to compute the dot product.")
            return sum(a * b for a, b in zip(self.components, other.components))
        elif isinstance(other, (int, float)):
            return Vector(*(a * other for a in self.components))
        else:
            raise TypeError("Operand must be a Vector or a scalar.")

    def __rmul__(self, scalar):
        """
        Scalar multiplication from the left.
        :param scalar: A number to multiply each component by.
        :return: A new vector with each component multiplied by the scalar.
        """
        return self * scalar

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
# Create vectors
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

# Print the vector
print(v1)          # Output: Vector(1, 2, 3)

# Addition
v3 = v1 + v2
print(v3)          # Output: Vector(5, 7, 9)

# Subtraction
v4 = v2 - v1
print(v4)          # Output: Vector(3, 3, 3)

# Dot product
dot_product = v1 * v2
print(dot_product) # Output: 32

# Scalar multiplication
v5 = 3 * v1
print(v5)          # Output: Vector(3, 6, 9)

# Magnitude
print(v1.magnitude())  # Output: 3.7416573867739413

# Normalization
v_unit = v1.normalize()
print(v_unit)      # Output: Vector(0.267, 0.534, 0.801)