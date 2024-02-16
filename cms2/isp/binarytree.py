from node import BSTNode
from linkedstack import LinkedStack

class LinkedBinaryTree:
    def __init__(self) -> None:
        self._root = None

    def add_left(self, node: BSTNode, left: str) -> None:
        left = BSTNode(left)
        node.left = left

    def add_right(self, node: BSTNode, right: str) -> None:
        right = BSTNode(right)
        node.right = right

    def get_left(self, node: BSTNode) -> BSTNode | None:
        return node.left

    def get_right(self, node: BSTNode) -> BSTNode | None:
        return node.right

    def set_root(self, node: BSTNode) -> None:
        root = BSTNode(node)
        self._root = root

    def get_root(self):
        return self._root

    def inorder(self, node: BSTNode):
        if node is None:
            return []
        result = []
        result.extend(self.inorder(node.left))
        result.append(node.data)
        result.extend(self.inorder(node.right))
        return result

    def is_leaf(self, node: BSTNode) -> bool:
        return node.left is None and node.right is None

    def leaf_paths(self, node: BSTNode):
        def make_path(stack: LinkedStack):
            mes = ''
            while not stack.isEmpty():
                mes += f"{stack.pop().data}-"
            return mes[:-1]

        if self.is_leaf(node):
            discovered = set()
            stack = LinkedStack()
            current_node = self.get_root()
            while current_node is not None:
                if current_node.data == node.data:
                    stack.add(node)
                    return make_path(stack)
                discovered.add(current_node.data)
                stack.add(current_node)
                if current_node.left is not None and current_node.left.data not in discovered:
                    current_node = current_node.left
                elif current_node.right is not None and current_node.right.data not in discovered:
                    current_node = current_node.right
                else:
                    stack.pop()
                    current_node = stack.pop()




