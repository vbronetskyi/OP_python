"""Lab 6, ex 7"""
def generate_pascal_triangle(numb: int) -> list :
    """
    The function should return a triangle as a list of lists,
    starting at the top level.

    >>> print(generate_pascal_triangle(5))
    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    >>> print(generate_pascal_triangle(0))
    []
    """
    if numb <= 0 or not isinstance(numb, int): return []
    pascal_lst = []
    num = [1]
    enum = 0
    while enum < numb-1 :
        pascal_lst.append(num)
        num = [sum(j) for j in zip([0]+num, num+[0])]
        enum +=1
    pascal_lst.append(num)
    return pascal_lst

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
