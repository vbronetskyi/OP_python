"""Lab_13.2"""

def read_file(str_file):
    """funct read corect file"""
    with open(str_file, "r", encoding = 'utf-8') as file:
        file_read, names, number = file.readlines(), [], []

        for elem in file_read:
            elem = elem.replace("(", "").replace(")", "").replace("\n", "")\
                .replace(" ", "").split("\t")

            for num in elem:
                if num.isnumeric():
                    elem.remove(num)
                    number.append(int(num))
                    elem.append(int(num))
            names.append(elem)

        return names[1:],number[1:]

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

def top_three_name(path):
    """
    returns the three most popular names in 2007
    """
    names, numbs_of_names = read_file(path)
    selection_sort(numbs_of_names)
    lst, solut = [], set()

    for numb in numbs_of_names:
        for name in names:
            if numb in name:
                if not name in lst:
                    lst.append(name)
                else: continue

    lst = lst[::-1]
    lst = lst[:3]
    top_three_names = [item for sublist in lst for item in sublist]
    for i in top_three_names:
        if not isinstance(i, int):
            solut.add(i)

    return solut

def special_names (file_path):
    """
    returns names that occur only once
    """
    names, _ = read_file(file_path)
    spec_names, countir= set(), 0

    for name in names:
        if name[1] == 1:
            spec_names.add(name[0])
            countir += 1

    return countir, spec_names

def popular_letter(file_path):
    """
    Returns the letter that starts
    with the largest number of names
    """
    names, _ = read_file(file_path)
    lst_countir, child_names, countir, numb_of_childs= [], [], 0, 0
    alfabet = ["А", "Б", "В", "Г", "Д", "Е", "Є", "Ж",
    "З", "І", "Й", "К", "Л", "М", "Н", "О", "П", "Р",
    "С", "Т", "У", "Ф", "Х", "Ц", "Ч", "Ш", "Щ", "Ю", "Я"]


    for letter in alfabet:
        for name in names:
            if name[0].startswith(letter):
                numb_of_childs += name[1]
                countir += 1

        lst_countir.append(countir)
        child_names.append(numb_of_childs)

        numb_of_childs, countir = 0, 0
        name = alfabet[lst_countir.index(max(lst_countir))]
        most_popular_name = child_names[lst_countir.index(max(lst_countir))]

    return name, max(lst_countir), most_popular_name

def find_names(file_path):
    """
    return solution of all functions
    """
    return top_three_name(file_path), special_names(file_path), popular_letter(file_path)
# print((find_names('boy_names')))
