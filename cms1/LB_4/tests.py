import math

def four_lines_area(k1, c1, k2, c2, k3, c3, k4, c4):
    """
    (float, float ... float) -> float

    Finding the area of a convex quadrilateral.
    """
    # Сreate pairs
    variant_of_pairs = [lines_intersection(k1, c1, k2, k2),
    lines_intersection(k3, c3, k4, c4),
    lines_intersection(k2, c2, k3, c3),
    lines_intersection(k4, c4, k1, c1)]

    # Сreate lists
    size = []
    size.append(distance(variant_of_pairs[0][0], variant_of_pairs[0][1], variant_of_pairs[1][0], variant_of_pairs[1][1]))
    size.append(distance(variant_of_pairs[0][0], variant_of_pairs[0][1], variant_of_pairs[2][0], variant_of_pairs[2][1]))
    size.append(distance(variant_of_pairs[0][0], variant_of_pairs[0][1], variant_of_pairs[3][0], variant_of_pairs[3][1]))
    size.append(distance(variant_of_pairs[1][0], variant_of_pairs[1][1], variant_of_pairs[2][0], variant_of_pairs[2][1]))
    size.append(distance(variant_of_pairs[2][0], variant_of_pairs[2][1], variant_of_pairs[3][0], variant_of_pairs[3][1]))
    size.append(distance(variant_of_pairs[1][0], variant_of_pairs[1][1], variant_of_pairs[3][0], variant_of_pairs[3][1]))
    
    #We check the parallelism of the lines and the correct implementation of the lists.
    #Call the function quadrangle_area
    if k1 == k2 == k3 or k1 == k2 == k4 or k2 == k2 == k4:
        return 0
    elif (size[0] and size[1] and size[2] and size[3] and size[4] and size[5]) != None:
        return quadrangle_area(size[0], size[3],  size[4],  size[2],  size[1],  size[5])
    else:
        return 0


def lines_intersection(k1, c1, k2, c2):
    """
    (float, ... float) -> float
    Function for finding the point of intersection of two straight lines
    """
    
    try:
        x = (c2 - c1) / (k1 - k2)
        y = k1 * x + c1
        return (round(x, 2), round(y, 2))
    except ZeroDivisionError:
        return None


def distance(x1, y1, x2, y2):
    """
    (float, ... float) -> float
    Function to find the distance between two points
    """
    return round(math.sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2), 2))



def quadrangle_area(a, b, c, d, f1, f2):
    """
    (float, ... float) -> float
    Function for finding the area of a quadrilateral
    """
    try:
        return round(math.sqrt((4 - pow(f1, 2) * pow(f2, 2) - pow((pow(b, 2) + pow(d, 2) - pow(c, 2)), 2) / 4), 2))
    except ValueError:
        return None