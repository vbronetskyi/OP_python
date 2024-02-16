"""The function should return the length of the path and the number of turns
clockwise (right) and counter-clockwise
clockwise (left) that must be done when moving
from point A to point B, through points K, L, M, N"""
from math import sqrt

def turns(points):
    """
    accepts a list of tuples where each tuple is
    coordinates of a point on the plane.
    find left and right turns
    >>> turns([(2, 2), (4, 8), (11, 1), (8, 10), (4, 4), (12, 6)])
    (1, 3)
    """
    left_turns, right_turns = 0, 0
    try:
        for indx, cords in enumerate(points):
            if indx == 0:
                continue
            if cords[0]*points[indx+1][1]-points[indx+1][0]*cords[1]>0:
                left_turns+=1
            elif cords[0]*points[indx+1][1]-points[indx+1][0]*cords[1]<0:
                right_turns+=1
    except IndexError:
        pass
    return left_turns, right_turns

def find_path(points):
    """
    accepts a list of tuples where each tuple is
    coordinates of a point on the plane. The function should
    return path length and number of turns
    >>> find_path([(2, 2), (12, 6), (4, 8), (11, 1), (8, 10), (4, 4)])
    (41.17, 1, 3)
    """
    #find path
    last_point = points.pop(1)
    points.append(last_point)
    vectors = []
    try:
        for indx, cords in enumerate(points):
            vector = sqrt(pow(points[indx+1][0]-cords[0], 2)+pow(points[indx+1][1]-cords[1], 2))
            vectors.append(vector)
    except IndexError:
        pass
    vector_len = round(sum(vectors), 2)
    #find turns
    num_left, num_right = turns(points)

    return vector_len, num_left, num_right

if __name__ == "__main__":
    print(find_path([(2, 2), (1, 6), (4, 1), (11, 3),(8, 10), (4, 4), (1, 1)]))
