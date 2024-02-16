"""graph_case_study_testing"""

import graph
import algorithms
from linkedstack import LinkedStack

def read_file(path):
    """
    Function that reads a file and transforms it into a graph.
    """
    with open(path, 'r', encoding='utf-8') as file:
        data = file.read().strip().split("\n")
        data_2d = [i[:-1].split(' (') for i in data][1:]

    # transform to the graph
    new_graph = graph.LinkedDirectedGraph()

    for elem in data_2d:
        new_graph.addVertex(elem[0])
        if elem[1] != 'none':
            new_graph.addVertex(elem[1])
            new_graph.addEdge(elem[0], elem[1], 0)

    return new_graph

def bfs_test():
    """
    bfs algo test
    """
    test_graph = read_file("stanford_cs.txt")
    return bfs(test_graph, test_graph.getVertex("MATH19"))

def dfs_test():
    """
    dfs algo test
    """
    test_graph = read_file("stanford_cs.txt")
    stack = LinkedStack()
    return algorithms.dfs(test_graph, test_graph.getVertex("MATH19"), stack)

def topological_sort_test():
    """
    topological sort test 
    """
    test_graph = read_file("stanford_cs.txt")
    return algorithms.topoSort(test_graph)

def bfs(g, start_vertex):
    """
    bfs implementation
    """
    stack1 = LinkedStack()
    stack2 = LinkedStack()

    start_vertex.setMark()
    stack1.push(start_vertex)

    while not stack1.isEmpty() or not stack2.isEmpty():
        if not stack1.isEmpty():
            current_vertex = stack1.pop()
        else:
            current_vertex = stack2.pop()

        # Process the vertex (e.g., print its label)
        print(current_vertex.getLabel())

        for neighbor in g.neighboringVertices(current_vertex.getLabel()):
            if not neighbor.isMarked():
                neighbor.setMark()

                # Alternate between stack1 and stack2 for adding neighbors
                if stack1.isEmpty():
                    stack1.push(neighbor)
                else:
                    stack2.push(neighbor)


# print(read_file("stanford_cs.txt"))

print(bfs_test())
# print(topological_sort_test())