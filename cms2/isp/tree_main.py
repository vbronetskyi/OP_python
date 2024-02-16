class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def add_left(self, data):
        node = Node(data)
        if self.root is None:
            self.root = node
        else:
            self.root.left = node

    def add_right(self, data):
        node = Node(data)
        if self.root is None:
            self.root = node
        else:
            self.root.right = node

    def get_left(self):
        if self.root is None:
            return None
        return self.root.left

    def get_right(self):
        if self.root is None:
            return None
        return self.root.right

    def set_root(self, data):
        self.root = Node(data)

    def get_root(self):
        if self.root is None:
            return None
        return self.root.data

    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(node.data)
            self.inorder(node.right)

    def is_leaf(self, node):
        return node is not None and node.left is None and node.right is None

    def leaf_paths(self):
        if self.root is None:
            return

        stack = [(self.root, None)]
        paths = {}

        while stack:
            node, parent = stack.pop()

            if self.is_leaf(node):
                path = []
                while node is not None:
                    path.append(node.data)
                    node = paths[node]
                path.reverse()
                print('-'.join(str(x) for x in path))

            paths[node] = parent

            if node.right is not None:
                stack.append((node.right, node))
            if node.left is not None:
                stack.append((node.left, node))

tree = BinaryTree()
tree.set_root(1)
tree.add_left(2)
tree.add_right(3)
tree.get_left().add_left(4)
tree.get_left().add_right(5)
tree.get_right().add_left(6)
tree.get_right().add_right(7)
tree.get_right().get_left().add_right(8)

tree.leaf_paths()
