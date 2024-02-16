'''def dict_reader_dict(file_dict):


    """
    returns a dictionary as a dictionary
    """
    solut = {}
    for i in file_dict:
        if file_dict[0]:
            solut[len(file_dict[0])] = set()
        solut[file_dict[0]].update(file_dict[1])
    solut = {i:solut[i] for i in sorted(solut)}
    return solut

def dict_invert(dct):
    """
    returns the pronunciation dictionary as a dictionary

    >>> dict_invert({'WATER':{('W','A','T','E','R')}})
    {1: {('WATER', ('W','A','T','E','R'))}}
    >>> dict_invert({'AABERG': {('AA1', 'B', 'ER0', 'G')}, 'A.': {('EY1',)},
                  'A': {('EY1',), ('AH0',)}, 'A42128': {('EY1', 'F', 'AO1',
                  'R', 'T', 'UW1', 'W', 'AH1', 'N', 'T', 'UW1', 'EY1', 'T')},
                  'AAA': {('T', 'R', 'IH2', 'P', 'AH0', 'L', 'EY1')}})
{1: {('A.', ('EY1',)), ('AABERG', ('AA1', 'B', 'ER0', 'G')), ('AAA', ('T', 'R',\
 'IH2', 'P', 'AH0', 'L', 'EY1')),
('A42128', ('EY1', 'F', 'AO1', 'R', 'T', 'UW1', 'W', 'AH1', 'N', 'T', 'UW1', 'EY1',\
 'T'))},
2: {('A', ('EY1',)), ('A', ('AH0',))}}
    >>> dict_invert(dict_reader_tuple('cmudict.txt')) == dict_invert(dict_reader_\
dict('cmudict.txt'))
    True
    """
    if isinstance(dct, dict):
        solut = {}
    elif isinstance(dct, list):
        solut_1 = {}
        for i in dct:
            if i[0] not in dct:
                solut_1[i[0]] = set()
            solut_1[i[0]].update({tuple(i[2])})
        dct = solut_1
        solut = {}
    for i in dct:
        if len(dct[i]) not in dct:
            solut[len(dct[i])] = set()
        solut[len(dct[i])].update(zip([i]*len(dct[i], dct[i])))
    solut = {i:solut[i] for i in sorted(solut)}
    return solut
'''
def add_edge(graph, edge):
    """
    (dict, tuple) -> dict

    Add a new edge to the graph and return new graph.

    >>> add_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (1, 3))
    {1: [2, 5, 3], 2: [1, 4], 3: [4, 1], 4: [2, 3], 5: [1]}
    """
    if edge[0] in graph:
        graph[edge[0]].append(edge[1])
    else:
        graph[edge[0]] = [edge[1]]
    if edge[1] in graph:
        graph[edge[1]].append(edge[0])
    else:
        graph[edge[1]] = [edge[0]]
    return graph
print(add_edge({1: [2], 2: [1]}, (1, 3)))
