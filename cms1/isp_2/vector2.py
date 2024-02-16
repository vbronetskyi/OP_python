"""
The modul should return the length of the path and the
number of clockwise (right) turns and the number of counterclockwise
(left) turns to make when moving from point A to point B
"""
def define_vector(point1, point2):
    '''
    Creates vector (start - point1, end - point2)
    >>> define_vector((2, 2), (4, 8))
    (2, 6)
    >>> define_vector((2, 0), (3, 5))
    (1, 5)
    >>> define_vector((-1, -1), (3, 5))
    (4, 6)
    '''

    vector = (point2[0] - point1[0], point2[1] - point1[1])
    return vector

def find_engle(point1, point2, point3):
    '''
    Returns sinus of engle between vertex given with three points,
    point 2 is end of one verctor and start of another
    >>> find_engle((1, 2), (3, 4), (4, 6))
    0.31622715852984296
    >>> find_engle((-1, 2), (-3, 4), (4, 6))
    -0.8741563741982514
    >>> find_engle((1, 2), (-3, -4), (4, 6))
    0.02272140523007824
    '''
    vector = define_vector(point1, point2)
    vector2 = define_vector(point2, point3)

    length_1 = length(vector)
    length_2 = length(vector2)

    multiply = (vector[0] * vector2[1]) - (vector2[0] * vector[1])
    return multiply / (length_1 * length_2)

def length(vector):
    """
    Returns length of vector
    >>> length((7, -7))
    9.89949
    >>> length((-1, -7))
    7.07107
    >>> length((-1, 0))
    1.0
    """
    return round((vector[0]**2 + vector[1]**2)**(0.5),5)

def find_path(points):
    '''
    Finds path which goes through every point in points
    and number of turns to left and to right
    >>> find_path([(2, 2), (12, 6), (4, 8), (11, 1),(8, 10), (4, 4)])
    (41.17, 1, 3)
    >>> find_path([(2, 2), (12, 6), (4, 8), (11, 1),(8, 10), (4, 4), (1, 1)])
    (49.25, 2, 3)
    >>> find_path([(2, 2), (1, 6), (4, 1), (11, 3),(8, 10), (4, 4), (1, 1)])
    (33.59, 2, 3)
    '''
    left = 0
    right = 0
    way = 0
    points.append(points.pop(1))
    for i in range(len(points)-1):
        if i < len(points) - 2:
            engle = find_engle(points[i], points[i+1], points[i+2])
            if engle < 0:
                right += 1
            else:
                left += 1
        way += (length(define_vector(points[i], points[i+1])))
    return round(way, 2), right, left

print(find_path([(2, 2), (1, 6), (4, 1), (11, 3),(8, 10), (4, 4), (1, 1)]))
# import doctest
# doctest.testmod()
