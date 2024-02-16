"""
modul 2
Жадібний алгоритм
Help the aliens steal people
"""
def read_file(path):
    """
    >>> read_file("smart_people.txt")
    {'Elon Musk': '165', 'Mark Zuckerberg': '152', 'Will Smith': '157', \
'Marilyn vos Savant': '186', 'Judith Polgar': '170', 'Quentin Tarantino': \
'163', 'Bill Gates': '160', "Conan O'Brien": '160', 'Emma Watson': '132', \
'Barack Obama': '137'}
    """
    set_of_people = {}
    with open(path, 'r',encoding="utf8") as file:
        file.readline()
        while True:
            line_f = file.readline().replace('\n', '').split(',')
            if line_f != ['']:
                set_of_people[line_f[0]]=line_f[1]
            else:
                break
    return set_of_people
# print(read_file("smart_people.txt"))
def selection_sort(set_to_do):
    """
    Sort the list using the selection sort method.
    Return a sorted list
    """
    def swap(list_, min_inx_, inx_):
        """
        swap elements in list
        """
        list_[inx_], list_[min_inx_] = list_[min_inx_], list_[inx_]
        return list_

    for inx in range(len(set_to_do)):
        min_inx = inx
        for j in range(inx + 1, len(set_to_do)):
            if set_to_do[j][1] < set_to_do[min_inx][1]:
                min_inx = j
        swap(set_to_do, min_inx, inx)
    return set_to_do

def rescue_people(smarties, limit_qt):
    """
    >>> rescue_people({"Steve Jobs": 160, "Albert Einstein": 160, \
"Sir Isaac Newton": 195, "Nikola Tesla": 189},500)
    (2, [['Sir Isaac Newton', 'Nikola Tesla'], ['Albert Einstein', 'Steve Jobs']])
    >>> rescue_people({"Steve Jobs": 160, "Albert Einstein": 160, \
"Sir Isaac Newton": 195, "Nikola Tesla": 189, "Tatyana Gerasimova": 200, \
"Konstantin Hrytsak": 200},500)
    (3, [['Konstantin Hrytsak', 'Tatyana Gerasimova'], ['Sir Isaac Newton', \
'Nikola Tesla'], ['Albert Einstein', 'Steve Jobs']])
    """
    if smarties == {}:
        print("The aliens decided that there are no intelligent \
            people on earth (they don't want to kidnap anyone)")
        return None
    list_of_transact = []
    for name in smarties.keys():
        if smarties[name] < 130:
            del smarties[name]
        else:
            list_of_transact.append(((name), smarties[name]))
    selection_sort(list_of_transact)
    list_of_transact = list_of_transact[-1::-1]
    iq_on_boat, iterat = 0,0
    solut_lst= []
    for people in list_of_transact:
        if iq_on_boat+people[1] > limit_qt:
            iterat +=1
            iq_on_boat = 0
        if iq_on_boat == 0:
            solut_lst.append([])
        solut_lst[iterat].append(people[0])
        iq_on_boat +=people[1]
    return len(solut_lst), solut_lst
print(rescue_people({"Steve Jobs": 160, "Albert Einstein": 160, \
"Sir Isaac Newton": 195, "Nikola Tesla": 189},500))

def main():
    """The main function"""
    read_file('smart_people.txt')
    rescue_people({"Steve Jobs": 160, "Albert Einstein": 160, \
    "Sir Isaac Newton": 195, "Nikola Tesla": 189},500)

if __name__ == "__main__":
    main()
    import doctest
    print(doctest.testmod())
