"""
A library to find reflexive, symmetric and transitive relations,
equivalence classes of a relation
"""
import doctest
import time


def read_file(name):
    """
    (str) -> list
    Gets a text matrix and returns it as a list
    """
    txt_matrix = [i.replace('\n', '') for i in open(name, "r").readlines()]
    matrix = []
    for i in range(len(txt_matrix)):
        line = str(txt_matrix[i])
        txt_matrix[i] = [_ for _ in line]
        line_math = []
        for j in range(len(txt_matrix[i])):
            line_math.append(int(txt_matrix[i][j]))
        matrix.append(line_math)
    return matrix


def write_matrix_to_file(matrix, name):
    """
    (list) -> str
    Gets the matrix in the form of a list, and writes it to a file
    """
    txt_matrix = open(name, "w")
    for line in range(len(matrix)):
        txt_matrix.writelines(str(matrix[line]).replace(' ', '').replace('[', '').replace(']', '').replace(',', '')+'\n')


def find_reflexive_closure(matrix: list) -> list:
    """
    Returns the reflexive closure of a given matrix

    Parameters
    ----------
    matrix : list
        A list of lists representing a matrix

    Returns
    -------
    list
        A list of lists representing the reflexive closure of the given matrix

    Doctests
    --------
    >>> find_reflexive_closure([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
    [[1, 1, 0], [0, 1, 1], [1, 0, 1]]
    >>> find_reflexive_closure([[0, 1, 1], [0, 0, 1], [0, 0, 0]])
    [[1, 1, 1], [0, 1, 1], [0, 0, 1]]
    """
    for i in range(len(matrix)):
        matrix[i][i] = 1
    write_matrix_to_file(matrix, 'Reflexive.txt')
    return matrix


def find_symmetric_closure(matrix: list) -> list:
    """
    Returns the symmetric closure of a given matrix

    Parameters
    ----------
    matrix : list
        A list of lists representing a matrix

    Returns
    -------
    list
        A list of lists representing the symmetric closure of the given matrix

    Doctests
    --------
    >>> find_symmetric_closure([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
    [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
    >>> find_symmetric_closure([[1, 1, 1], [0, 0, 1], [0, 0, 0]])
    [[1, 1, 1], [1, 0, 1], [1, 1, 0]]
    """
    # Replace every [j][i] with [i][j] if [i][j] is 1
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 1:
                matrix[j][i] = 1
    write_matrix_to_file(matrix, 'Symmetric.txt')
    return matrix


def find_transitive_closure(matrix: list, write_to_file: bool = True) -> list:
    """
    Find a transitive closure of a matrix

    Parameters
    ----------
    matrix : list
        A matrix

    Returns
    -------
    list
        A transitive closure of a matrix

    Doctests
    --------
    >>> find_transitive_closure([[1, 1, 0], [0, 1, 1], [0, 0, 1]])
    [[1, 1, 1], [0, 1, 1], [0, 0, 1]]
    >>> find_transitive_closure([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    >>> find_transitive_closure([[0, 1, 0], [1, 1, 0], [0, 0, 1]])
    [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    >>> find_transitive_closure([[1, 1],[1, 0]])
    [[1, 1], [1, 1]]
    >>> find_transitive_closure([[0, 0], [0, 0]])
    [[0, 0], [0, 0]]
    >>> find_transitive_closure([[1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 0, 0], [0, 0, 1, 1]])
    [[1, 0, 1, 1], [1, 1, 1, 1], [1, 0, 1, 1], [1, 0, 1, 1]]
    """
    length = len(matrix)
    # Make a copy of the matrix
    new_matrix = [_[:] for _ in matrix]
    # Warshall's algorithm
    for k in range(length):
        for i in range(length):
            for j in range(length):
                if new_matrix[i][k] and new_matrix[k][j]:
                    new_matrix[i][j] = 1
    # If it wasn't told to not write to a file, write the matrix to a file
    if write_to_file:
        write_matrix_to_file(new_matrix, 'Transitive.txt')
    return new_matrix


def split_equivalent_relation(matrix: list) -> list:
    """
    Split an equivalence relation into equivalence classes.

    Parameters
    ----------
    matrix : list
        A list of lists representing an equivalence relation.

    Returns
    -------
    list
        A list of lists representing the equivalence classes.

    Doctests
    --------
    >>> split_equivalent_relation([[1, 1, 0], [1, 1, 0], [0, 0, 1]])
    [{1, 2}, {3}]
    >>> split_equivalent_relation([[0, 1, 1], [1, 1, 1], [0, 1, 1]])
    [{1, 3}, {2}]
    >>> split_equivalent_relation([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    [{1}, {2}, {3}]
    """
    classes: list = []
    # Check every 2 rows. If they are equivalent, add them to the same class
    for i, row_i in enumerate(matrix):
        for j, row_j in enumerate(matrix):
            if row_i == row_j:
                # If there is no class already, create a new one
                if all((i + 1 not in c for c in classes)):
                    classes.append(set([i + 1, j + 1]))
                # Else add to an existing one
                else:
                    for equivalence_class in classes:
                        if i + 1 in equivalence_class:
                            equivalence_class.add(j + 1)
    _write_equivalence_classes(classes)
    return classes


def _write_equivalence_classes(classes: list):
    """Write the equivalence classes to a file."""
    with open('Equivalence classes.txt', 'w', encoding='utf-8') as file:
        file.write(str(classes))


def is_transitive(matrix: list) -> bool:
    """
    Check if a relation is transitive.

    Parameters
    ----------
    matrix : list
        A list of lists representing a relation.

    Returns
    -------
    bool
        True if the relation is transitive, False otherwise.

    Doctests
    --------
    >>> is_transitive([[1, 0, 1, 1], [1, 1, 1, 1], [1, 0, 1, 1], [1, 0, 1, 1]])
    True
    >>> is_transitive([[1, 1], [1, 1]])
    True
    >>> is_transitive([[1, 1], [1, 0]])
    False
    """
    # If the transitive closure is the same as the original, return True
    if matrix == find_transitive_closure(matrix, False):
        return True
    return False


def find_number_of_transitive(n: int) -> int:
    """
    Count the number of transitive closures on a set of n elements.

    Parameters
    ----------
    n: int
        The number of elements in the set.

    Returns
    -------
    int
        The number of transitive closures.

    Doctests
    --------
    # >>> find_number_of_transitive(4)
    # 3994
    >>> find_number_of_transitive(3)
    171
    >>> find_number_of_transitive(2)
    13
    """

    def _get_matrixes(j: int) -> list:
        """
        Get the matrixes for all closures of ixj

        Parameters
        ----------
        j: int
            The number of columns and rows in the matrix.

        Returns
        -------
        list
            A list of lists representing the matrixes of ixj.
        """
        transitive_matrixes = []
        # Generate all possible lines of 1 and 0 of length j
        numbers = []
        for _ in range(2 ** (j * j)):
            numbers.append(f"{str(bin(_))[2:]:0>{j*j}}")

        # Convert every line to a matrix, split every j elements into a row
        for _ in range(len(numbers)):
            # Append an empty matrix
            matrix: list = []
            for k in range(0, j):
                # For every row, append an empty list(line)
                matrix.append([])
                for q in range(0, j):
                    # Get every element of the number and append it to the row
                    # An element should be taken from j*k to j*(k+1)
                    # This way we split the number into rows
                    matrix[k].append(int(numbers[_][k * j : (k + 1) * j][q]))
            if is_transitive(matrix):
                # If the matrix is a transitive closure, add it to the list
                transitive_matrixes.append(matrix)
        return transitive_matrixes

    # Get all possible matrixes of nxn, that are transitive
    matrixes: list = _get_matrixes(n)
    # Check every matrix if it is transitive
    return len(matrixes)


def _main():
    """Run doctests."""
    print(doctest.testmod())


if __name__ == "__main__":
    _main()
