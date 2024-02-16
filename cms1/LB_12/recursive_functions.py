"""Lab_12.1"""
from typing import List

def create_table(rows: int, cols: int) -> List[list]:
    """
    building a table of numbers with the size of rows on cols.
    A[0][j] = 1, A[i][0] = 1
    A[i][j] = A[i-1][j] + A[i][j-1]
    returns a list of lists
    >>> create_table(4, 6)
    [[1, 1, 1, 1, 1, 1], [1, 2, 3, 4, 5, 6], [1, 3, 6, 10, 15, 21], [1, 4, 10, 20, 35, 56]]
    >>> create_table(3, 3)
    [[1, 1, 1], [1, 2, 3], [1, 3, 6]]
    >>> create_table(3,7)
    [[1, 1, 1, 1, 1, 1, 1], [1, 2, 3, 4, 5, 6, 7], [1, 3, 6, 10, 15, 21, 28]]
    """
    #exit
    if rows == 1:
        solut = list()
        solut += [cols*[1]]
        return solut
    #recurs
    solut = create_table(rows-1, cols)
    add_rows = [1]

    for i in range(1, cols):
        add_rows+=[add_rows[i-1]+solut[-1][i]]
    solut +=[add_rows]

    return solut
#print(create_table(3,7))

def flatten(lst: List[list] or list) -> list:
    """
    accepts a list which may contain other lists
    which may also contain other lists and which may also contain lists.
    returns a single list consisting of all non-empty elements of each of the input lists
    >>> flatten([1,[2]])
    [1, 2]
    >>> flatten([1,2,[3,[4,5],6],7])
    [1, 2, 3, 4, 5, 6, 7]
    >>> flatten([[]])
    []
    >>> flatten(3)
    3
    """
    # if lst not a list, - return lst
    if not isinstance(lst, list):
        return lst

    solut = list()
    for numb in lst:
        if not isinstance(numb, list):
            solut.append(numb)
        else:
            solut.extend(flatten(numb))
    return solut
#print(flatten(3))

# import doctest
# (doctest.testmod())
