from fignya.graph_map import *

# Testing the graph_map module

# Reading the file and building the graph
file_path = 'stanford_cs.txt'
graph = read_file(file_path)

# Testing BFS
print("BFS:")
bfs_result = bfs(graph, 'CS108')
print(bfs_result)

# Testing DFS
print("DFS:")
dfs_result = dfs(graph, 'CS108')
print(dfs_result)

# Testing Topological Sort
print("Topological Sort:")
topological_sort_result = topological_sort(graph)
print(topological_sort_result)
