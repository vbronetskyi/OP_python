from collections import deque
from graph import Graph
def read_file(filename):
    graph = Graph()
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            if line:
                parts = line.split(' ')
                course = parts[0]
                prerequisites = parts[1].strip('()').split(',')
                for prerequisite in prerequisites:
                    graph.add_edge(course, prerequisite)
    return graph

def bfs(graph, start_vertex):
    visited = set()
    queue = deque([start_vertex])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            neighbors = graph.get_neighbors(vertex)
            queue.extend(neighbors)

    return visited

def dfs(graph, start_vertex, visited=None):
    if visited is None:
        visited = set()

    visited.add(start_vertex)
    neighbors = graph.get_neighbors(start_vertex)

    for neighbor in neighbors:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

    return visited

def topological_sort(graph):
    visited = set()
    stack = []

    def dfs_topological_sort(vertex):
        visited.add(vertex)
        neighbors = graph.get_neighbors(vertex)

        for neighbor in neighbors:
            if neighbor not in visited:
                dfs_topological_sort(neighbor)

        stack.append(vertex)

    for vertex in graph.graph:
        if vertex not in visited:
            dfs_topological_sort(vertex)

    return stack[::-1]

def bfs_test():
    graph = read_file('stanford_cs.txt')
    start_vertex = 'CS108'
    result = bfs(graph, start_vertex)
    print(f"BFS traversal starting from {start_vertex}: {result}")

def dfs_test():
    graph = read_file('stanford_cs.txt')
    start_vertex = 'CS108'
    result = dfs(graph, start_vertex)
    print(f"DFS traversal starting from {start_vertex}: {result}")

def topological_sort_test():
    graph = read_file('stanford_cs.txt')
    result = topological_sort(graph)
    print(f"Topological sorting: {result}")

def run_tests():
    bfs_test()
    dfs_test()
    topological_sort_test()

run_tests()
