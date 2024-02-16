"""Lab_12_1.Test_graph_map"""

import graph as grf
import bfs
import dfs
import topological_sort as tp_sotr

def read_file(path):
    """
    read a file and transforms it into a graph
    """
    with open(path, 'r', encoding='utf-8') as file:
        data = file.read().strip().split("\n")
        data_2d = [i[:-1].split(' (') for i in data]

    new_graph = grf.Graph()

    for elem in data_2d:
        ver1 = new_graph.insert_vertex(elem[0])

        if elem[1] != 'none':
            ver2 = new_graph.insert_vertex(elem[1])
            new_graph.insert_edge(ver1, ver2)

    return new_graph

def bfs_test():
    """
    Tests the breadth-first search algorithm
    """
    test_graph = read_file("stanford_cs.txt")
    test = bfs.BFS_complete(test_graph)
    return test


def dfs_test():
    """
    Tests the depth-first search algorithm
    """
    test_graph = read_file("stanford_cs.txt")
    test = dfs.DFS_complete(test_graph)
    return test

def topological_sort_test():
    """
    Tests the topological sort algorithm
    """
    test_graph = read_file("stanford_cs.txt")
    test = tp_sotr.topological_sort(test_graph)
    return test

def main():
    """The main func"""
    file = read_file("stanford_cs.txt")
    # print(file)
    print(bfs_test(), '\n')
    print(dfs_test(), '\n')
    print(topological_sort_test(), '\n')

main()
    