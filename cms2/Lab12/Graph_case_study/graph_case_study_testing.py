"""Lab_12_2.Test_graph_case_study"""
import graph as grf
import algorithms
from linkedstack import LinkedStack as link_st

def read_file(path):
    """
    read a file and transforms it into a graph
    """
    with open(path, 'r', encoding='utf-8') as file:
        data = file.read().strip().split("\n")
        data_2d = [i[:-1].split(' (') for i in data]

    # transform to the graph
    new_graph = grf.LinkedDirectedGraph()

    for elem in data_2d:
        new_graph.addVertex(elem[0])
        if elem[1] != 'none':
            new_graph.addVertex(elem[1])
            new_graph.addEdge(elem[0], elem[1], 0)

    return new_graph


def dfs_test():
    """
    Tests the depth-first search algorithm
    """
    test_graph = read_file("stanford_cs.txt")
    stack = link_st()
    return algorithms.dfs(test_graph, test_graph.getVertex("MATH19"), stack)

def topological_sort_test():
    """
    Tests the topological sort algorithm
    """
    test_graph = read_file("stanford_cs.txt")
    return algorithms.topoSort(test_graph)

def bfs(g, start_vertex):
    """
    my breadth-first search algorithm
    """
    first_stack = link_st()
    second_stack = link_st()
    start_vertex.setMark()
    first_stack.push(start_vertex)

    while not first_stack.isEmpty() or not second_stack.isEmpty():
        if first_stack.isEmpty(): current_vertex = second_stack.pop()
        else: current_vertex = first_stack.pop()

        print(current_vertex.getLabel())

        for neighbor in g.neighboringVertices(current_vertex.getLabel()):
            if not neighbor.isMarked():
                neighbor.setMark()
                if first_stack.isEmpty(): first_stack.push(neighbor)
                else: second_stack.push(neighbor)

def main():
    """the main func"""
    def bfs_test():
        """
        Tests the breadth-first search algorithm
        """
        test_graph = read_file("stanford_cs.txt")
        return bfs(test_graph, test_graph.getVertex("CS107"))
    print(read_file("stanford_cs.txt"), '\n')
    # test_graph = read_file("stanford_cs.txt")
    # print(bfs(test_graph, test_graph.getVertex("MATH19")))
    print(bfs_test(), '\n')
    print(topological_sort_test(), '\n')
main()
