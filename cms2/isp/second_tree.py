import csv

class Node:
    def __init__(self, year, percent):
        self.year = year
        self.percent = percent
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, year, percent):
        if self.root is None:
            self.root = Node(year, percent)
        else:
            self._insert(year, percent, self.root)

    def _insert(self, year, percent, current_node):
        if year < current_node.year:
            if current_node.left is None:
                current_node.left = Node(year, percent)
            else:
                self._insert(year, percent, current_node.left)
        elif year > current_node.year:
            if current_node.right is None:
                current_node.right = Node(year, percent)
            else:
                self._insert(year, percent, current_node.right)
        else:
            current_node.percent = percent

    def find(self, year, percent):
        if self.root is not None:
            return self._find(year, percent, self.root)
        else:
            return None

    def _find(self, year, percent, current_node):
        if year == current_node.year:
            if current_node.percent < percent:
                return current_node
            elif current_node.left is not None:
                return self._find(year, percent, current_node.left)
            else:
                return None
        elif year > current_node.year and current_node.right is not None:
            return self._find(year, percent, current_node.right)
        elif year < current_node.year and current_node.left is not None:
            return self._find(year, percent, current_node.left)
        else:
            return None

def population_trees(file_path):
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)  # Skip header
        trees = []
        for i in range(3):  # Create 3 trees
            trees.append(BST())
        for row in csv_reader:
            year = int(row[0])
            # percent = int(row[2])
            for i in range(3):
                if row[i+3] != '':
                    trees[i].insert(year, float(row[i + 3]))
        return trees
population_trees('Kosiv_state.csv')
