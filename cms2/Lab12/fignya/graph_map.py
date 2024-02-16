"""Lab_12.ex_1.graph_map"""

class Graph:
    """
    Клас, що представляє граф.

    Атрибути:
        graph (dict): Словник, що містить вершини та їх сусідів.

    Методи:
        add_edge(source, destination): Додає ребро між вершинами.
        get_neighbors(vertex): Повертає список сусідів заданої вершини.
        get_vertices(): Повертає список всіх вершин у графі.
    """

    def __init__(self):
        """
        Конструктор
        """
        self.graph = {}

    def add_edge(self, source, destination):
        """
        Додає ребро між вершинами у граф.

        Параметри:
            source (str): Вершина, з якої виходить ребро.
            destination (str): Вершина, до якої веде ребро.

        Повертає:
            None
        """
        if source not in self.graph:
            self.graph[source] = []
        self.graph[source].append(destination)

    def get_neighbors(self, vertex):
        """
        Повертає список сусідів заданої вершини у графі.

        Параметри:
            vertex (str): Вершина, для якої потрібно отримати сусідів.

        Повертає:
            list: Список сусідів заданої вершини.
        """
        if vertex in self.graph:
            return self.graph[vertex]
        return []

    def get_vertices(self):
        """
        Повертає список всіх вершин у графі.

        Повертає:
            list: Список всіх вершин у графі.
        """
        return list(self.graph.keys())


def read_file(file_path):
    """
    Зчитує файл та створює граф на його основі.

    Параметри:
        file_path (str): Шлях до файлу.

    Повертає:
        Graph: Граф, побудований на основі даних з файлу.
    """
    graph = Graph()
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            if line:
                course, prerequisites = line.split(' (')
                prerequisites = prerequisites.rstrip(')').split(', ')
                for prerequisite in prerequisites:
                    graph.add_edge(prerequisite, course)
    return graph


def bfs(graph, start_vertex):
    """
    Виконує обхід графа в ширину (BFS).

    Параметри:
        graph (Graph): Граф, який потрібно обійти.
        start_vertex (str): Початкова вершина для початку обходу.

    Повертає:
        list: Список вершин, упорядкованих у порядку обходу BFS.
    """
    visited = []
    queue = [start_vertex]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.append(vertex)
            neighbors = graph.get_neighbors(vertex)
            queue.extend(neighbors)
    return visited


def dfs(graph, start_vertex):
    """
    Виконує обхід графа в глибину (DFS).

    Параметри:
        graph (Graph): Граф, який потрібно обійти.
        start_vertex (str): Початкова вершина для початку обходу.

    Повертає:
        list: Список вершин, упорядкованих у порядку обходу DFS.
    """
    visited = []

    def dfs_recursive(vertex):
        visited.append(vertex)
        neighbors = graph.get_neighbors(vertex)
        for neighbor in neighbors:
            if neighbor not in visited:
                dfs_recursive(neighbor)

    dfs_recursive(start_vertex)
    return visited


def topological_sort(graph):
    """
    Виконує топологічне сортування графа.

    Параметри:
        graph (Graph): Граф, для якого потрібно виконати топологічне сортування.

    Повертає:
        list: Список вершин, упорядкованих за топологічним порядком.
    """
    visited = set()
    stack = []

    def topological_sort_recursive(vertex):
        visited.add(vertex)
        neighbors = graph.get_neighbors(vertex)
        for neighbor in neighbors:
            if neighbor not in visited:
                topological_sort_recursive(neighbor)
        stack.append(vertex)

    vertices = graph.get_vertices()
    for vertex in vertices:
        if vertex not in visited:
            topological_sort_recursive(vertex)

    return stack[::-1]
