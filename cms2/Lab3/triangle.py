"""Lab_3.Ex_4"""
import point
class Triangle:
    """
    Class
    >>> triangle = Triangle(point.Point(1,1), point.Point(3,1), point.Point(2,3))
    """
    def __init__(self, point1, point2, point3) -> None:
        """
        constructor
        >>> triangle = Triangle(point.Point(1,1), point.Point(3,1), point.Point(2,3))
        """
        self.edge1 = ((point2.x-point1.x)**2+(point2.y-point1.y)**2)**0.5
        self.edge2 = ((point3.x-point2.x)**2+(point3.y-point2.y)**2)**0.5
        self.edge3 = ((point1.x-point3.x)**2+(point1.y-point3.y)**2)**0.5

    def is_triangle(self)->bool:
        """
        try triangle: exacly cordinates
        >>> triangle.is_triangle()
        True
        """
        if self.edge1 + self.edge2 > self.edge3 and self.edge1 + self.edge3\
        > self.edge2 and self.edge3 + self.edge2 > self.edge1 and self.edge1\
        > 0 and self.edge2 > 0 and self.edge3> 0:
            return True
        return False
    def perimeter(self):
        """
        calculates the perimeter by vertex
        >>> triangle.perimeter()
        6.47213595499958
        """
        return self.edge1 + self.edge2 + self.edge3
    def area(self):
        """
        calculates the area of a triangle using the Heron formula
        >>> triangle = Triangle(point.Point(1,1), point.Point(3,1), point.Point(2,3))
        >>> triangle.area()
        2.0
        """
        p_num = (self.edge1 + self.edge2 + self.edge3)/2
        return (p_num*(p_num-self.edge1)*(p_num-self.edge2)*(p_num-self.edge3))**0.5

triangle = Triangle(point.Point(1,1), point.Point(3,1), point.Point(2,3))
print(triangle.area())
if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
