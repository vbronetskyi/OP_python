"""Lab_13.1"""
from typing import List
import random

def linear_search(list_of_values, value):
    """
    (lst, int) -> int
    Return the index of the first value that occurs in
    the given list. If there is none, then returns -1
    (use algorithm linear search)
    >>> linear_search([1, 2, 3, 4, 5, 6, 5], 5)
    4
    >>> linear_search([1, 2, 3], 99)
    -1
    """
    for inx, elem in enumerate(list_of_values):
        if elem == value: return inx
    if value not in list_of_values:
        return -1

def merge(list1, list2):
    """
    (list, list) -> list
    The function combines two lists into one sorted list
    >>> merge([1,4,9],[2,8])
    [1, 2, 4, 8, 9]
    >>> merge([1,3,5,7,9],[2,4,6,8])
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    solut_lst = list()
    i, j = 0, 0
    while len(list1) + len(list2) > len(solut_lst):
        if list2[j] > list1[i]:
            solut_lst.append(list1[i])
            if list1[i] == list1[-1]:
                solut_lst += list2[j:]
            else: i += 1
        else:
            solut_lst.append(list2[j])
            if list2[j] == list2[-1]:
                solut_lst += list1[i:]
            else: j += 1
    return solut_lst

def merge_sort(lst: list) -> List[int]:
    """
    (list, int)->List[int]
    Sorting the list using the merge method
    return sorted list
    >>> merge_sort([1, 0, 99, 9, 6, 3])
    [0, 1, 3, 6, 9, 99]
    >>> merge_sort([1,-1,0])
    [-1, 0, 1]
    """
    if len(lst) in (0, 1):
        return lst
    lst1 = merge_sort(lst[:len(lst)//2])
    lst2 = merge_sort(lst[len(lst)//2:])
    return merge(lst1, lst2)


def binary_search(list_of_values, value):
    """
    (lst, int) -> int
    Return the index of the first value that occurs in
    the given list. If there is none, then returns -1
    (use algorithm binary search)

    >>> binary_search([-2, -1, 0, 1, 2], 1)
    3
    >>> binary_search([1, 2, 3, 4, 5, 6, 5], 5)
    4
    >>> binary_search([1, 2, 3], 999)
    -1
    """
    if value not in list_of_values:
        return -1
    else:
        least, last= list_of_values[0],list_of_values[-1]
        while last > least-1:
            if value == (least + last)//2:
                return list_of_values.index((least + last)//2)
            elif value < (least + last)//2:
                last = (least + last)//2 - 1
            elif value > (least + last)//2:
                least = (least + last)//2 +1


def selection_sort(lst):
    """
    Sort the list using the selection sort method.
    Return a sorted list
    >>> selection_sort([1, 0, 99, 9, 6, 3])
    [0, 1, 3, 6, 9, 99]
    >>> selection_sort([1,-1,0])
    [-1, 0, 1]
    """
    def swap(list_, min_inx_, inx_):
        """
        swap elements in list
        """
        list_[inx_], list_[min_inx_] = list_[min_inx_], list_[inx_]
        return list_

    for inx in range(len(lst)):
        min_inx = inx
        for j in range(inx + 1, len(lst)):
            if lst[j] <lst[min_inx]:
                min_inx = j
        swap(lst, min_inx, inx)
    return lst

def quick_sort(lst):
    """
    Sort the list using the quick sort method.
    Return a sorted list
    >>> quick_sort([1, 0, 99, 9, 6, 3])
    [0, 1, 3, 6, 9, 99]
    >>> quick_sort([1,-1,0])
    [-1, 0, 1]
    """
    if len(lst) > 1:
        rand_num = random.randrange(len(lst))

        defin = lst[rand_num]

        least_numbs = [numb for _, numb in enumerate(lst) if numb <= defin and _ != rand_num]
        big_numbs = [numb for _, numb in enumerate(lst) if numb > defin]
        return quick_sort(least_numbs) + [defin] + quick_sort(big_numbs)
    else: return lst

# if __name__ == "__main__":
#     import doctest
#     doctest.testmod(verbose = True)
