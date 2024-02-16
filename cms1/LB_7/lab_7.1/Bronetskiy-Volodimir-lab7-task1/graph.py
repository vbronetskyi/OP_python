# Complete all of the following functions. Currently they all just
# 'pass' rather than explicitly return value, which means that they
# implicitly return None.

def get_graph_from_file(file_name):
    """
    (str) -> (list)
    Read graph from file and return a list of edges.
    >>> get_graph_from_file("data1.txt")
    [[1, 2], [3, 4], [1, 5]]
    """
    with open(file_name, 'r',encoding="utf8") as file:
        lst = file.read().split('\n')
        lst = [i.split(',') for i in lst]
        for i in range(len(lst)): lst[i] = [int(j) for j in lst[i]]
        return lst

def to_edge_dict(edge_list):
    """
    (list) -> (dict)
    Convert a graph from list of edges to dictionary of vertices.

    >>> to_edge_dict([[1, 2], [3, 4], [1, 5], [2, 4]])
    {1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}
    """
    solut = {}
    for i in edge_list:
        if i[0] in solut:
            solut[i[0]].append(i[1])
        else: solut[i[0]] = [i[1]]
        if i[1] in solut:
            solut[i[1]].append(i[0])
        else: solut[i[1]] = [i[0]]
    return solut

def is_edge_in_graph(graph, edge):
    """
    (dict, tuple) -> bool

    Return True if graph contains a given edge and False otherwise.

    >>> is_edge_in_graph({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (3, 1))
    False
    """
    if edge[0] in graph and edge[1] in graph[edge[0]]:
        return True
    else: return False

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

def del_edge(graph, edge):
    """
    (dict, tuple) -> (dict)

    Delete an edge from the graph and return a new graph.

    >>> del_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (2, 4))
    {1: [2, 5], 2: [1], 3: [4], 4: [3], 5: [1]}
    """
    if edge[1] in graph and edge[0] in graph[edge[1]]: graph[edge[1]].remove(edge[0])
    if edge[0] in graph and edge[1] in graph[edge[0]]: graph[edge[0]].remove(edge[1])
    return graph

def add_node(graph, node):
    """
    (dict, int) -> (dict)

    Add a new node to the graph and return a new graph.

    >>> add_node({1: [2], 2: [1]}, 3)
    {1: [2], 2: [1], 3: []}
    """
    pass

def del_node(graph, node):
    """
    (dict, int) -> (dict)

    Delete a node and all incident edges from the graph.

    >>> del_node({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, 4)
    {1: [2, 5], 2: [1], 3: [], 5: [1]}
    """
    pass

def convert_to_dot(graph):
    """
    (dict) -> (None)

    Save the graph to a file in a DOT format.
    """
    with open('graph.dot', 'w', encoding='utf8') as file:
        file.write(str(graph))
    return None
