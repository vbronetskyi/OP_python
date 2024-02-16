"""Lab 6, ex 3"""
def happy_number(number: int) -> bool:
    """
    Returns true if the ticket is lucky
    >>> happy_number(12345)
    False
    >>> happy_number(43211234)
    True
    >>> happy_number(191234)
    True
    """
    number = str(number)
    number = number.zfill(8)
    sum1, sum2 = 0, 0
    for i in range(len(number)):
        if i<4: sum1+=int(number[i])
        else: sum2+=int(number[i])
    if sum1 == sum2: return True
    return False

def count_happy_numbers(number: int) -> int:
    """
    Returns the number of lucky tickets in the interval n
    """
    sum_numb = 0
    for i in range(1, number+1):
        if happy_number(i): sum_numb +=1
    return sum_numb

def happy_numbers(min_num: int, max_num: int) -> list:
    """
    Returns a list of lucky tickets in the given range of ticket numbers
    >>> happy_numbers(1, 11111)
    [10001, 10010, 10100, 11000]
    """
    solut = []
    for i in range(min_num, max_num+1):
        if happy_number(i): solut.append(i)
    return solut

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
