from string import ascii_uppercase
from string import ascii_lowercase

def get_number():
    number = 28
    return number

# ****************************************
# Problem 2
# ****************************************
def compare_char(ch1, ch2):
    """
    (str, str) -> bool
    Compare two char by their position in alphabet. Return True if letter
    ch2 appears before ch1 and False otherwise. If neither ch1 nor ch2 are
    letters function should return None.

    >>> compare_char('a', 'z')
    False
    >>> compare_char('c', 'B')
    True
    >>> compare_char('d', 'ad')

    >>> compare_char('2', 2)

    """
    solut = None
    flg1 = False
    flg2 = False

    for i in range(26):
        if ch2 in (ascii_uppercase[i], ascii_lowercase[i]):
            flg2 = True
        if ch1 in (ascii_uppercase[i], ascii_lowercase[i]):
            flg1 = True

    if flg1 & flg2:
        for i in range(26):
            if ch2 in (ascii_uppercase[i], ascii_lowercase[i]):
                solut = True
                break
            if ch1 in (ascii_uppercase[i], ascii_lowercase[i]):
                solut = False
                break
    return solut



# ****************************************
# Problem 6
# ****************************************
def remove_spaces(s):
    """
    str -> str
    Remove all additional spaces in string and return a new string without additional spaces.
    If argument is not a string function should return None.

    >>> remove_spaces("I'll make     him an     offer he can't refuse.")
    I'll make him an offer he can't refuse.
    >>> remove_spaces("Great    men     are    not born great, they grow great...")
    Great men are not born great, they grow great...
    >>> remove_spaces(2015)

    """
    solut = str()

    if isinstance(s, str):
        for i in range(len(s)):
            if s[i]== ' ' and s[i+1] == ' ':
                continue
            else:
                solut += s[i]
    else:
        solut = None

    return solut



# ****************************************
# Problem 8
# ****************************************
def number_of_sentences(s):
    """
    str -> str
    Return number of sentence in the string. If argument is not a string function should
    return None.

    >>> number_of_sentences("Revenge is a dish that tastes best when served cold.")
    1
    >>> number_of_sentences("Never hate your enemies. It affects your judgment.")
    2
    >>> number_of_sentences(2015)

    """
    amount = 0

    if isinstance(s, str):
        for i in range(len(s)):
            if s[i]== '.':
                amount+=1
    else:
        amount = None

    return amount



# ****************************************
# Problem 9
# ****************************************
def replace_with_stars(s):
    """
    str -> str
    Replace symbols in string with stars. If argument is not a string function should
    return None.

    >>> number_of_sentences("Revenge is a dish that tastes best when served cold.")
    ****************************************************
    >>> number_of_sentences("Never hate your enemies. It affects your judgment.")
    **************************************************
    >>> number_of_sentences(2015)

    """
    changed_text = str()

    if isinstance(s, str):
        for i in range(len(s)):
            changed_text += '*'

    else:
        changed_text = None

    return changed_text



# ****************************************
# Problem 12
# ****************************************
def exclude_letters(s1, s2):
    """
    (str, str) -> str
    Delete all letter from string s2 in string s1. If arguments aren't strings function should
    return None.

    >>> exclude_letters("aaabb", "b")
    aaa
    >>> exclude_letters("abcc", "cczzyy")
    ab
    >>> exclude_letters(2015, "sasd")

    """

    solut = str()
    flg = True

    if isinstance(s1, str) and isinstance(s2, str):
        for i in range(len(s1)):
            for j in range(len(s2)):
                if s2[j] == s1[i]:
                    flg = False
            if flg:
                solut += s1[i]
            flg = True
    else:
        solut = None
    return solut



# ****************************************
# Problem 13
# ****************************************
def create_string(lst):
    """
    list -> str
    Create and return string from histogrma of letters. If argument isn't list of 26 positive
    integer numbers function should return None.

    >>> create_string([0,1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    bcc
    >>> create_string([4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4])
    aaaazzzz
    >>> create_string([4, 0, 0, 0, 0, 0])

    """

    solut = str()
    lst_cr = list(lst)

    if len(lst_cr) == 26:
        q = 0
        for i in range(26):
            if lst[i] != 0:
                for j in range(lst[i]):
                    solut += ascii_lowercase[q]
                q += 1
            elif lst[i] == 0:
                q += 1
    else:
        solut = None
    return solut



# ****************************************
# Problem 15
# ****************************************
def find_intersection(s1, s2):
    """
    (str, str) -> str
    Find and returs string of all letters in alphabetic order that
    are present in both strings. If arguments aren't strings function
    should return None.

    >>> find_intersection("aaabb", "bbbbccc")
    b
    >>> find_intersection("aZAbc", "zzYYxp")
    z
    >>> find_intersection("sfdfsdf", 2015)

    """

    solut = str()
    asci1 = str()
    asci2 = str()

    if isinstance(s1, str) and isinstance(s2, str):
# Sort s1 and s2 + delete extra characters
        for i in range(26):
            for j in range(len(s1)):
                if s1[j] == ascii_lowercase[i] or s1[j] == ascii_uppercase[i]:
                    asci1 += ascii_lowercase[i]
                    break
        for i in range(26):
            for j in range(len(s2)):
                if s2[j] == ascii_lowercase[i] or s2[j] == ascii_uppercase[i]:
                    asci2 += ascii_lowercase[i]
                    break

        # filling solution
        for i in range(len(asci1)):
            for j in range(len(asci2)):
                if asci1[i] == asci2[j]:
                    solut += asci1[i]
                    break
    else:
        solut = None

    return solut



# ****************************************
# Problem 16
# ****************************************
def find_union(s1, s2):
    """
    (str, str) -> str
    Find and return string of all letters in alphabetic order that
    are present in either strings. If arguments aren't strings function should
    return None.

    >>> find_union("aaabb", "bbbbccc")
    abc
    >>> find_union("aZAbc", "zzYYxp")
    AYZabcpxz
    >>> find_union("sfdfsdf", 2015)

    """

    solut = None
    asci1 = str()
    asci2 = str()

    if isinstance(s1, str) and isinstance(s2, str):
        solut = str()
        for i in range(26):
            for j in range(len(s1)):
                if s1[j] == ascii_lowercase[i] or s1[j] == ascii_uppercase[i]:
                    asci1 += s1[j]
        for i in range(26):
            for j in range(len(s2)):
                if s2[j] == ascii_lowercase[i] or s2[j] == ascii_uppercase[i]:
                    asci2 += s2[j]

        # filling solution
        #uppercase
        asci1 += asci2
        for i in range(26):
            for j in range(len(asci1)):
                if asci1[j] == ascii_uppercase[i]:
                    solut += ascii_uppercase[i]
                    break
        #lowercase
        for i in range(26):
            for j in range(len(asci1)):
                if asci1[j] == ascii_lowercase[i]:
                    solut += ascii_lowercase[i]
                    break
    else:
        solut = None

    return solut



# ****************************************
# Problem 23
# ****************************************
def one_swap_sorting(sequence):
    """
    (str) -> bool
    Design a function one_swap_sorting(sequence) that takes a list and
    returns True if swapping two elements of the list will make it a
    sorted list, and False otherwise. It is necessary to take into
    account the case when the list is empty.

    >>> one_swap_sorting([0,1,2,3])
    False
    >>> one_swap_sorting([])
    False
    >>> one_swap_sorting([42])
    False
    >>> one_swap_sorting([3,2])
    True
    >>> one_swap_sorting([2,2])
    False
    >>> one_swap_sorting([5,2,3,4,1,6])
    True
    >>> one_swap_sorting([1,2,3,5,4])
    True
    """
    #List sort
    sort_list = []

    for i in range(len(sequence)):
        if sequence[i] != ' ' and sequence[i] != ',' and sequence[i] != '[' and sequence[i] != ']':
            sort_list.append(sequence[i])
    sequence = sort_list.copy()
    sort_list.sort()

    #Determine the number of replacements
    changes_numb = 0
    for i in range(len(sequence)):
        if sequence[i] != sort_list[i]:
            changes_numb += 1

    #Solution
    return changes_numb == 2



# ****************************************
# Problem 24
# ****************************************
def numbers_Ulam(n):
    """
    (int) -> list
    Develop a function numbers_ulam(n) to find n Ulam numbers. The
    function should return a list of n Ulam numbers. Ulam's number
    is an element of a sequence of integers. These numbers are named
    after the mathematician Stanislav Ulam, who described them in 1964.
    The standard sequence of Ulam numbers is the numbers 1 and 2.

    >>> numbers_Ulam(10)
    [1, 2, 3, 4, 6, 8, 11, 13, 16, 18]
    >>> numbers_Ulam(2)
    [1, 2]
    >>> numbers_Ulam(1)
    [1]
    """

    n = int(n)
    ulam_numbers = [1, 2]

    q = 3
    if n == 1:
        ulam_numbers.pop()
    else:
        #fill in the list
        while len(ulam_numbers) != n:
            count = 0
            #check whether the number is the number of ulam
            for j in range(len(ulam_numbers) - 1):
                for k in range(j + 1, len(ulam_numbers)):
                    if ulam_numbers[j] + ulam_numbers[k] == q:
                        count += 1
                    if count > 1:
                        break
                if count > 1:
                    break

            if count == 1:
                ulam_numbers.append(q)
            q+=1

    return ulam_numbers



# ****************************************
# Problem 25
# ****************************************
def sqr_numb(numb):
    """
    (int) -> int
    Returns sum of squares of digits

    >>> sqr_numb(12)
    5
    """
    numb_sqrt = 0
    while numb:
        numb_sqrt += (numb % 10) * (numb % 10)
        numb = numb // 10
    return numb_sqrt

def happy_number(n):
    """
    (int) -> bool
    Design a function happy_number(n) to check whether the number n
    is lucky. The function should accept a number and return True if
    the number is lucky and False otherwise. A natural number is called
    a lucky number if the sequence that begins with this number, and
    each subsequent term of which is the sum of the squares of the
    revious digits, contains a term equal to one.

    >>> happy_number(32)
    True
    >>> happy_number(33)
    False
    >>> happy_number(13)
    True
    >>> happy_number(12)
    False
    """

    n = int(n)
    slow = n
    fast = n

    while True:
        slow = sqr_numb(slow)
        fast = sqr_numb(sqr_numb(fast))
        if slow == fast:
            break

    return slow == 1



# ****************************************
# Problem 26
# ****************************************
def sum_of_divisors(n, lst):
    """
    (int, str) -> int
    Find and return sum of all odd numbers in the list, that are divisible by n.

    >>> sum_of_divisors(3, [2, 0, 1, 5])
    0
    >>> sum_of_divisors(5, [2, 0, 1, 5])
    5
    >>> sum_of_divisors(7, [])
    0

    """
    n = int(n)
    change_list = []

    for i in range(len(lst)):
        if lst[i] != ' ' and lst[i] != ',' and lst[i] != '[' and lst[i] != ']':
            change_list.append(int(lst[i]))

    sum_of_numbers = 0
    for i in range(len(change_list)):
        if change_list[i] % 2 == 1:
            if change_list[i] % n == 0:
                sum_of_numbers += change_list[i]

    return sum_of_numbers



if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
