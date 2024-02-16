"""line.py"""
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
    def __eq__(self, other: object):
        if other is None or self is None:
            return False
        return self.x, self.y==other.x, other.y

class Line(Point):
    """line"""
    def __init__(self, directs) -> None:
        """Constructor"""
        self.direct = directs[0]
        self.direct1 = directs[1]
        super().__init__(directs[0].x, directs[0].y)
        # self.x, self.y = intersect(self, other)
    # def __init__(self, x, y) -> None:
    #     super().__init__(x, y)

    def intersect(self, other):
        """Find intersection of two lines"""
        x1, y1 = self.direct.x, self.direct.y
        x2, y2 = self.direct1.x, self.direct1.y
        x3, y3 = other.direct.x, other.direct.y
        x4, y4 = other.direct1.x, other.direct1.y

        denom = (y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1)
        if denom == 0:  # lines are parallel
            return self.direct

        ua = ((x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)) / denom
        ub = ((x2 - x1) * (y1 - y3) - (y2 - y1) * (x1 - x3)) / denom

        if ua < 0 or ua > 1 or ub < 0 or ub > 1:  # intersection point is not within line segments
            return None
        x = x1 + ua * (x2 - x1)
        y = y1 + ua * (y2 - y1)
        return Point(x, y)
line1 = Line([Point(0, 0), Point(10, 10)])
line2 = Line([Point(0, 10), Point(10, 0)])
assert line1.intersect(line2) == Point(0, 0)
assert line2.intersect(line1) == Point(0, 0)
assert line1.intersect(line2) == Point(5.0, 5.0)
assert line1.intersect(line2)
assert line1.intersect(line1) == line1
