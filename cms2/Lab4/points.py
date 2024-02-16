"""Lab4.4_points"""

class Point:
    """
    father
    >>> point1 = Point(17, 2)
    """
    def __init__(self, x, y) -> None:
        """
        constructor
        >>> assert (point1.y, point1.x) == (2, 17)
        """
        self.x = x
        self.y = y
    def __str__(self) -> str:
        """
        return messege
        >>> assert str(point1) == "Point in two-dimensional space with coordinates (17, 2)"
        """
        return "Point in two-dimensional space with coordinates (%s, %s)" %(self.x, self.y)
    def vector_length(self):
        """
        finds length vector between two points
        >>> assert Point(3, 4).vector_length() == 5
        >>> assert Point(4, 5).vector_length() == 6.4
        >>> assert Point(6, -12).vector_length() == 13.42
        >>> assert Point(100, 0).vector_length() == 100
        """
        return round((self.x**2+self.y**2)**0.5, 2)
    def __eq__(self, other):
        """
        operator ==
        >>> assert Point(5, 4) == Point3D(5, 4, 0)
        >>> assert Point3D(5, 4, 0) == Point(5, 4)
        """
        return self.vector_length() == other.vector_length()
    def __repr__(self) -> str:
        """
        dunder method defines behavior when you pass an
        instance of a class to the 2 coord
        >>> assert str([point1, point2]) == "[Point(x=17, y=2), Point(x=17, y=4, z=2)]"
        """
        return f"Point(x={self.x}, y={self.y})"
# print(Point(4, 5).vector_length())

point1 = Point(17, 2)
# assert (point1.y, point1.x) == (2, 17)
# assert str(point1) == "Point in two-dimensional space with coordinates (17, 2)"
class Point3D(Point):
    """
    child
    >>> point2 = Point3D(17, 4, 2)
    """
    def __init__(self, x, y, z=0) -> None:
        """
        constructor
        >>> assert (point2.y, point2.z, point2.x) == (4, 2, 17)
        """
        super().__init__(x, y)
        self.z = z
    def __str__(self) -> str:
        """
        return message
        >>> assert str(point2) == "Point in three-dimensional space with coordinates (17, 4, 2)"
        """
        return "Point in three-dimensional space with coordinates (%s, %s, %s)" \
            %(self.x, self.y, self.z)
    def vector_length(self):
        """
        finds length vector between two points
        >>> assert Point3D(-6, -12, 0).vector_length() == 13.42, Point3D(-6, -12, 0).vector_length()
        >>> assert Point3D(3, 4, 12).vector_length() == 13
        >>> assert Point3D(-13, 14, -15).vector_length() == 24.29
        """
        return round((self.x**2+self.y**2+self.z**2)**0.5,2)
    def __eq__(self, other):
        """
        operator ==
        >>> assert Point(5, 4) == Point3D(5, 4, 0)
        >>> assert Point3D(5, 4, 0) == Point(5, 4)
        """
        return self.vector_length() == other.vector_length()

    def __repr__(self) -> str:
        """
        dunder method defines behavior when you pass an instance of a class to the
        >>> assert str([point1, point2]) == "[Point(x=17, y=2), Point(x=17, y=4, z=2)]"
        """
        return f"Point(x={self.x}, y={self.y}, z={self.z})"
assert Point(3, 4) == Point(3, 4)
assert Point(3, 4) != Point(2, 3)

assert Point(5, 4) == Point3D(5, 4, 0)
assert Point3D(5, 4, 0) == Point(5, 4)

assert Point(5, 4) != Point3D(5, 4, 1)
assert Point3D(5, 4, 1) != Point(5, 4)

assert Point3D(8, 7, 0) == Point3D(8, 7)
point2 = Point3D(17, 4, 2)
assert (point2.y, point2.z, point2.x) == (4, 2, 17)
assert str(point2) == "Point in three-dimensional space with coordinates (17, 4, 2)"
assert str([point1, point2]) == "[Point(x=17, y=2), Point(x=17, y=4, z=2)]"
if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
