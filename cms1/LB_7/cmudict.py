"""Lab_7.3"""

def dict_reader_tuple(file_dict):
    """
    returns a dictionary as a list of tuples with three elements
    >>> dict_reader_tuple('cmudict.txt')[:2]
    [('A', 1, ['AH0']), ('A.', 1, ['EY1'])]
    """
    file = open(file_dict, encoding='utf8')
    file = [i for i in file]
    file = [j.strip('\n') for j in file]
    result = []

    for i in range(len(file)) :
        file[i] = file[i].split(' ')
        file[i][1] = int(file[i][1])
        third_elem = file[i][2:]
        file[i] = file[i][:2]
        file[i].append(third_elem)
        file[i] = (file[i][0], file[i][1], file[i][2])
        result.append(file[i])
    return result

def dict_reader_dict(file_dict):
    """
    returns a dictionary as a dictionary
    >>> sorted(dict_reader_dict('cmudict.txt')["A"])
    [('AH0',), ('EY1',)]
    """
    solut: dict[str, set[tuple]] = {}
    dct = dict_reader_tuple(file_dict)
    for word, _, transcrip in dct:
        if word not in solut: solut[word] = set()
        solut[word].add(tuple(transcrip))
    return solut

def dict_invert2(dct):
    """
    invert dict
    """
    solut = {}
    for i in dct:
        if len(dct[i]) not in dct:
            solut[len(dct[i])] = set()
        solut[len(dct[i])].update(zip([i]*len(dct[i]), dct[i]))
    solut = {i:solut[i] for i in sorted(solut)}
    return solut

def dict_invert(dct):
    """
    returns the pronunciation dictionary as a dictionary

    >>> dict_invert({'WATER':{('W','A','T','E','R')}})
    {1: {('WATER', ('W', 'A', 'T', 'E', 'R'))}}
    >>> dict_invert(dict_reader_tuple('cmudict.txt')) == dict_invert(dict_reader_\
dict('cmudict.txt'))
    True
    """
    if isinstance(dct, dict): return dict_invert2(dct)
    elif isinstance(dct, list):
        solut_1 = {}
        for i in dct:
            if i[0] not in solut_1: solut_1[i[0]] = set()
            solut_1[i[0]].update({tuple(i[2])})
        return dict_invert2(solut_1)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
