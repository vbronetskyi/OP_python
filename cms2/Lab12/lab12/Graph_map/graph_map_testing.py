"""graph_map_testing"""

import graph
import bfs
import dfs
import topological_sort

def read_file(path):
    """
    Function that reads a file and transforms it into a graph.
    """
    with open(path, 'r', encoding='utf-8') as file:
        data = file.read().strip().split("\n")
        data_2d = [i[:-1].split(' (') for i in data][1:]

    # transform to the graph
    new_graph = graph.Graph()

    for elem in data_2d:
        ver1 = new_graph.insert_vertex(elem[0])
        if elem[1] != 'none':
            ver2 = new_graph.insert_vertex(elem[1])
            new_graph.insert_edge(ver1, ver2)

    return new_graph

def bfs_test():
    """
    bfs algo test
    """
    test_graph = read_file("stanford_cs.txt")
    test = bfs.BFS_complete(test_graph)
    return test


def dfs_test():
    """
    dfs algo test
    """
    test_graph = read_file("stanford_cs.txt")
    test = dfs.DFS_complete(test_graph)
    return test

def topological_sort_test():
    """
    topological sort test 
    """
    test_graph = read_file("stanford_cs.txt")
    test = topological_sort.topological_sort(test_graph)
    return test

if __name__ == "__main__":
    # file = read_file("stanford_cs.txt")
    # print(file)
    # print(bfs_test())
    # print(dfs_test())
    print(topological_sort_test())
