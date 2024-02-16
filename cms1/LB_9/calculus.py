"""Lab_9.2"""

# Complete all of the following functions. Currently they all just
# 'pass' rather than explicitly return value, which means that they
# implicitly return None.

def find_max_1(fun, points):
    """
    (function or str, list(number)) -> (number)
    Find and return maximal value of function f in points.

    >>> find_max_1(lambda x: x ** 2 + x, [1, 2, 3, -1])
    12
    """
    solut = []
    for i in range(len(points)) :
        solut.append(fun(points[i]))
    return max(sorted(solut))

def find_max_2(fun, points):
    """
    (function or str, list(number)) -> (number)
    Find and return list of points where function f has the maximal value.

    >>> find_max_2(lambda x: x ** 2 + x, [1, 2, 3, -1])
    [3]
    >>> find_max_2(lambda x: x ** 2 + x, [0, 4, 2, -6])
    [-6]
    """
    max_elem = 0
    for i in points:
        if fun(i)>max_elem:
            max_elem = i
    solut = []
    for i in points:
        if fun(i) == fun(max_elem):
            solut.append(i)
    return solut

def compute_limit(seq):
    """
    (function or str) -> (number)
    Compute and return limit of a convergent sequence.

    >>> compute_limit(lambda n: (n ** 2 + n) / n  2)
    1.0
    """
    solut = []
    i = 0
    while True :
        num = 10**i
        solut.append(seq(num))
        if i != 0 and abs(solut[i] - solut[i - 1]) < 0.001 :
            return round(solut[i], 2)
        i += 1

def compute_derivative(fun, x_x):
    """
    (function or str, numb) -> (numb)
    Compute and return derivative of function f in the point x_0

    >>> compute_derivative(lambda x: x ** 2 + x, 2)
    5.0
    """
    solut = []
    i = 0
    while True :
        d_x =  10  -i
        d_f = fun(x_x + d_x)
        d_f -= fun(x_x)
        der = d_f / d_x
        solut.append(der)
        if i != 0 and abs(solut[i] - solut[i - 1]) < 0.001:
            return round(solut[i], 2)
        i += 1

def get_tangent(fun, x_num):
    """
    (function or str, number) -> (str)
    Compute and return tangent line to function f in the point x_0.
    >>> get_tangent(lambda x: x ** 2 + x, 2)
    '5.0 * x - 4.0'
    """
    numb_f = fun(x_num)
    res_1 = - (x_num * compute_derivative(fun, x_num)) + numb_f
    res_2 = abs(- (x_num * compute_derivative(fun, x_num)) + numb_f)
    res_3 = abs(compute_derivative(fun, x_num))
    res_4 = compute_derivative(fun, x_num)
    if 0 > compute_derivative(fun, x_num):
        return f'- {res_3} * x - {res_1}'
    if 0 < compute_derivative(fun, x_num):
        return f'{res_4} * x - {res_2}'


def get_root(fun, first, last):
    """
    (function or str, number, number) -> (number)
    Compute and return root of the function f in the interval (a, b).
    >>> get_root(lambda x: x, -1, 1)
    0.0
    >>> get_root(lambda x: 2 * x - 1, -1, 1)
    0.5
    """
    if first > last:
        return 0
    elif fun(first)==0:
        return round(float(first), 2)
    return get_root(fun, first+1, last)

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
