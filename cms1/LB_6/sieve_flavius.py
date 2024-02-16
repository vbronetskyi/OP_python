"""Lb 6, ex 1"""
def sieve_flavius(num1):
    """
    (int)->list

    return list of lucky numbers

    >>> sieve_flavius(100)
    [1, 3, 7, 9, 13, 15, 21, 25, 31, 33, 37, 43, 49, 51, 63, 67, 69, 73, 75, 79, 87, 93, 99]
    >>> sieve_flavius(10)
    [1, 3, 7, 9]
    >>> sieve_flavius(0)
    []
    """
    lst = []
    for i in range(1, num1 + 1):
        if i%2 != 0: lst.append(i)
    num = 1
    while num < len(lst)- 1:
        lst1 = []
        for ind,mean in enumerate(lst):
            if (ind+1) % lst[num] != 0:
                lst1.append(mean)
        lst = lst1[:]

        num +=1

    return lst

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
