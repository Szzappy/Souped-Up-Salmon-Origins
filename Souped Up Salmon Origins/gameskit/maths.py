from math import sqrt


class Vector:
    """A unit of data that can represent either any 2D **locational** or **directional** values.

    :param x: Public - The X component of the Vector
    :param y: Public - The Y component of the Vector
    :type x: float
    :type y: float

    Example
    -----
    We can create a Vector like so::

    pos = Vector(10, 20)
    """

    def __init__(self, x: float=0, y: float=0) -> None:
        """The constructor for a Vector. Can accept *either* parameter, with a default
        value of 0 for any unspecified value.

        :param x: The X component of the Vector
        :param y: The Y component of the Vector
        :type x: float
        :type y: float
        """
        self.x = x
        self.y = y

    def add(self, other_vector: "Vector") -> None:
        """Adds another Vector to the current Vector (modifying the current Vector's
        instance attributes).

        :param other_vector: The Vector being added to this one
        :type other_vector: Vector

        Example
        -------
        Remember that the Vector is being added **too** the current Vector::

        vec1 = Vector(10, 10)
        vec2 = Vector(40, 60)
        vec1.add(vec2)
        print(vec1) # [50, 70]
        """
        self.x += other_vector.x
        self.y += other_vector.y

    def scale(self, scaler: float) -> None:
        """Scales the current Vector by a given float value.

        :param scaler: The amount to scale the Vector by
        :type scaler: float
        """
        self.x *= scaler
        self.y *= scaler

    def magnitude(self) -> float:
        """Calculates (and returns) the magnitude (length) of the Vector.

        :return: The magnitude of the Vector
        :rtype: float
        """
        return sqrt((self.x * self.x) + (self.y * self.y))

    def unit(self) -> "Vector":
        """Calculates (and returns) a Unit Vector for the current Vector.

        :return: The Unit Vector for the current Vector
        :rtype: Vector
        """
        magnitude = self.magnitude()
        return Vector(self.x / magnitude, self.y / magnitude)

    def normalise(self) -> None:
        """Converts the current Vector into a Unit Vector."""
        unit_vector = self.unit()
        self.x = unit_vector.x
        self.y = unit_vector.y

    def to_tuple(self):
        """Creates a **2D tuple** object for this Vector (containing the X and Y components).

        :return: A 2D tuple containing the X and Y components of this Vector
        :rtype: tuple
        """
        return self.x, self.y

    def __str__(self) -> str:
        """Creates a **str** object for this Vector (using default encoding).

        :return: The **str** form of the Vector
        :rtype: str"""
        return "[" + str(self.x) + ", " + str(self.y) + "]"


def distance(vector1: Vector, vector2: Vector) -> float:
    """Calculates the distance between two Vectors.

    :param vector1: The first Vector to calculate the distance between
    :param vector2: The second Vector to calculate the distance between
    :type vector1: Vector
    :type vector2: Vector
    :return: The distance between the two Vector parameters
    :rtype: float
    """
    x_line = vector2.x - vector1.x
    y_line = vector2.y - vector1.y
    return sqrt((x_line * x_line) + (y_line * y_line))


def clamp(value: float, min_value: float, max_value: float) -> float:
    """Ensures the **value** is contained within bounds (a minimum and a maximum).

    :param value: The value to *clamp*
    :param min_value: The lower bound
    :param max_value: The upper bound
    :type value: float
    :type min_value: float
    :type max_value: float
    :return: The clamped value
    :rtype: float
    """
    return max(min_value, min(value, max_value))


class Collider:
    """A collision polygon (more specifically, a rectangle) that can be attached to any object with a position and size.

    :param left: Public - The X position of the left side of the collision rectangle
    :param right: Public - The X position of the right side of the collision rectangle
    :param top: Public - The Y position of the top of the collision rectangle
    :param bottom: Public - The Y position of the bottom of the collision rectangle
    :type left: float
    :type right: float
    :type top: float
    :type bottom: float
    """
    def __init__(self, origin: Vector, size: Vector) -> None:
        """Creates a collision rectangle from an origin vector and a size vector.

        :param origin: The position of the object (the **centre** of it)
        :param size: The size of the object
        :type origin: Vector
        :type size: Vector
        """
        self.left = origin.x - size.x // 2
        self.right = origin.x + size.x // 2
        self.top = origin.y - size.y // 2
        self.bottom = origin.y + size.y // 2

    def move(self, amount: Vector) -> None:
        """Moves the Collider based off the amount.

        :param amount: The X and Y amount to move the Collider by
        :type amount: Vector
        """
        self.left += amount.x
        self.right += amount.x
        self.top += amount.y
        self.bottom += amount.y
