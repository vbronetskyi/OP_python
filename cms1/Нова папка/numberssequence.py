def pyramidal_numbers(length) :
    """
    This function will accept an int number and return a list
    """
    arr1 = []
    for i in range(length) :
        arr1.append(i)
    result = []
    for i in range(len(arr1)) :
        i = bin(i)
        if (i[-1] != '1') :
            i = list(i)
            ones = i.count('1')
            if ones % 2 == 0 :
                rap = list(map(int, i))
                up = "".join(rap)
                result += up
    return result