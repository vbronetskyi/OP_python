"""asdfgh"""
import copy
from typing import Dict, List


def connectivity_components(graph: dict[int, list[int]]) -> int:
    nodes=list(graph.keys())
    visited = []
    glob=[]
    def dfs(graph,node):
        if node not in visited:
            visited.append(node)
            for new_node in graph[node]:
                dfs(graph,new_node)
        return visited
    while nodes:
        temp=dfs(graph,nodes[0])
        glob.append(list(temp))
        nodes=[i for i in nodes if i not in visited]
        visited.clear()
    return glob



def find_vertex(graph: Dict[int, int]) -> List[int]:
    """
    Finds connected vertices in a graph, and as a result returns their list
    If they are missing, then returns None

    Input: graph - graph in the form of as dictionary
    Output: conect_vertices - list of connection vertices

    >>> find_vertex({1: [4, 3], 4: [1, 2, 3], 3: [1, 4], 2: [4]})
    [4]
    >>> find_vertex({1: [2], 2: [1, 3, 5], 3: [2, 4, 6], 4: [3], 5:[2, 6], 6:[3, 5]})
    [2, 3]
    >>> find_vertex({1: [2, 3], 2: [1, 4], 3: [1, 4], 4: [2, 3]})
    >>> find_vertex({1: [2], 2: [1, 3], 3: [2, 4], 4: [3, 5], 5: [4]})
    [2, 3, 4]
    """
    #Try graph. If graph not dictionary, return message
    if not isinstance(graph, dict):
        return "Graph must be a dictionary"
    #Create a new dictionary in order to store the edited graphs in it
    new_graph = copy.deepcopy(graph)

    #Create a list in which we will store connection vertices
    conect_vertices = []

    #Create a variable that will store the number of graph components
    lentgh_of_graph = len(connectivity_components(graph))

    #Cycle that iterates over dictionary keys (vertices)
    for key in graph.keys():
        #Cycle that iterates over key variables and removes a vertex from the graph
        for elem in graph[key]:
            new_graph[elem].remove(key)
        del new_graph[key]

        #If the number of components has changed after removing a vertex,
        #then we add this vertex to the list
        if len(connectivity_components(new_graph)) != lentgh_of_graph:
            conect_vertices.append(key)

        #Return the graph to its former content
        new_graph = copy.deepcopy(graph)

    #Checks if the list is empty
    if not conect_vertices:
        return None

    #Return list of connection vertices
    return conect_vertices

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
