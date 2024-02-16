import numpy as np

def bellman_ford_algo(nodes: list, edges: dict, start_vertex=0) -> dict:
    """
    Bellman-Ford algorithm
    >>> bellman_ford_algo([0, 1, 2, 3], {(0, 1): 1, (1, 0): 3, (1, 3):-2, (3,2):4, (2,1):3})
    """
    path_leng = {vrtx: np.inf for vrtx in nodes}
    path_leng[start_vertex] = 0
    path = {vrtx: [] for vrtx in nodes}
    path[start_vertex]=[start_vertex]
    # _ = len(nodes) #iterator
    # while _ >=1:
    for _ in range(len(nodes)-1):
        for (first_v, second_v), weitgh in edges.items():
            if path_leng[second_v] > path_leng[first_v] + weitgh:
                path_leng[second_v] = path_leng[first_v] + weitgh
                path[second_v] = path[first_v] + [second_v]
        # _-=1
    for (first_v, second_v), weitgh in edges.items():
        if path_leng[second_v] > path_leng[first_v] + weitgh:
            return None #becouse graph have negative cyrcle
    return path_leng, path
print(bellman_ford_algo([0, 1, 2, 3], {(0, 1): 1, (1, 0): 3, (1, 3):-2, (3,2):4, (2,1):3}))
