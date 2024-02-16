'''
module have 6 functions
'''
def read_file(str_file):
    '''
    funct read file
    >>> type(read_file('girl_names'))
    <class 'tuple'>
    '''
    with open(str_file, "r", encoding = 'utf-8') as f:
        file = f.readlines()
        list_name = []
        number = []
        for elem in file:
            elem = elem.replace("\n", "").replace("(", "").replace(")", "").replace(" ", "").split("\t")
            for num in elem:
                if num.isnumeric():
                    elem.remove(num)
                    number.append(int(num))
                    elem.append(int(num))
            list_name.append(elem)
        list_name = list_name[1:]
        number = number[1:]
        return list_name, number

def selection_sort(lst):
    '''
    Sorts a list with an algoritm of selection.
    >>> selection_sort([2, 4, 3, 1])
    [1, 2, 3, 4]
    >>> selection_sort([10000000, 6567, 0, 4567, 78])
    [0, 78, 4567, 6567, 10000000]
    '''
    for i in range(len(lst)):
        min_i = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_i]:
                min_i = j
        lst[min_i], lst[i] = lst[i], lst[min_i]
    return lst

def top(file_path):
    '''
    function return top 3 names
    >>> type(top("girl_names"))
    <class 'set'>
    '''
    list_name, number = read_file(file_path)
    res = []
    selection_sort(number)
    for i in number:
        for name in list_name:
            if i in name:
                if name in res:
                    continue
                else:
                    res.append(name)
    res = res[::-1]
    res = res[:3]
    top = [item for sublist in res for item in sublist]
    result = set()
    for i in top:
        if isinstance(i, str):
            result.add(i)
    return result

def one_name (file_path):
    '''
    function return names one
    >>> type(one_name("girl_names"))
    <class 'tuple'>
    '''
    list_name, counert = read_file(file_path)
    list_name = list_name
    one_names = set()
    counts = 0
    for name in list_name:
        if name[1] == 1:
            one_names.add(name[0])
            counts += 1
    res = (counts, one_names)
    return res

def name_letter(file_path):
    """
    function return names leter
    >>> type(name_letter("girl_names"))
    <class 'tuple'>
    """
    list_name, counert = read_file(file_path)
    alfabet = ["А", "Б", "В", "Г", "Д", "Е", "Є", "Ж", "З", "І", "Й", 
    "К", "Л", "М", "Н", "О", "П", "Р", "С", "Т", "У", "Ф", "Х", "Ц", "Ч", "Ш", "Щ", "Ю", "Я"]
    list_count = []
    counter = 0
    name_kids = []
    count_name_kids = 0
    for letter in alfabet:
        for name in list_name:
            if name[0].startswith(letter):
                counter += 1
                count_name_kids += name[1]
            # elif counter == 0:
            #     continue
            # else:
        list_count.append(counter)
        name_kids.append(count_name_kids)
        count_name_kids = 0
        counter = 0
        name = alfabet[list_count.index(max(list_count))]
        name_kids_max = name_kids[list_count.index(max(list_count))]
        res = (name, max(list_count), name_kids_max)
    return res

def file_names(file_path):
    '''
    return The last option
    >>> type(file_names('girl_names'))
    <class 'tuple'>
    '''
    top_3 = top(file_path)
    one_names = one_name(file_path)
    elem_3 = name_letter(file_path)
    res = (top_3, one_names, elem_3)
    return res

print((file_names('girl_names')))
