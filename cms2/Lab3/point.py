"""Lab_3.Ex_4_point"""

class Point:
    """
    >>> point = Point(1, 2)
    """
    def __init__(self, x, y) -> None:
        """
        Constructor of class
        >>> point.x
        1
        >>> point.y
        2
        """
        self.x = x
        self.y = y
    def __str__(self) -> str:
        """
        >>> point = Point(1, 2)
        >>> print(point)
        x-coordinate of the point is 1, and y-coordinate is 2.
        """
        return "x-coordinate of the point is %s, and y-coordinate is %s." %(self.x, self.y)
point = Point(1, 2)
if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
