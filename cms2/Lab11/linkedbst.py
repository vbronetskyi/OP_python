"""
File: linkedbst.py
Author: Ken Lambert
"""

from abstractcollection import AbstractCollection
from bstnode import BSTNode
from linkedstack import LinkedStack
from linkedqueue import LinkedQueue
from math import log


class LinkedBST(AbstractCollection):
    """An link-based binary search tree implementation."""

    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self._root = None
        AbstractCollection.__init__(self, sourceCollection)

    # Accessor methods
    def __str__(self):
        """Returns a string representation with the tree rotated
        90 degrees counterclockwise."""

        def recurse(node, level):
            s = ""
            if node != None:
                s += recurse(node.right, level + 1)
                s += "| " * level
                s += str(node.data) + "\n"
                s += recurse(node.left, level + 1)
            return s

        return recurse(self._root, 0)

    def __iter__(self):
        """Supports a preorder traversal on a view of self."""
        if not self.isEmpty():
            stack = LinkedStack()
            stack.push(self._root)
            while not stack.isEmpty():
                node = stack.pop()
                yield node.data
                if node.right != None:
                    stack.push(node.right)
                if node.left != None:
                    stack.push(node.left)

    def preorder(self):
        """Supports a preorder traversal on a view of self."""
        return None

    def inorder(self):
        """Supports an inorder traversal on a view of self."""
        lyst = list()

        def recurse(node):
            if node != None:
                recurse(node.left)
                lyst.append(node.data)
                recurse(node.right)

        recurse(self._root)
        return iter(lyst)

    def postorder(self):
        """Supports a postorder traversal on a view of self."""
        return None

    def levelorder(self):
        """Supports a levelorder traversal on a view of self."""
        return None

    def __contains__(self, item):
        """Returns True if target is found or False otherwise."""
        return self.find(item) != None

    def find(self, item):
        """If item matches an item in self, returns the
        matched item, or None otherwise."""

        def recurse(node):
            if node is None:
                return None
            elif item == node.data:
                return node.data
            elif item < node.data:
                return recurse(node.left)
            else:
                return recurse(node.right)

        return recurse(self._root)

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self._root = None
        self._size = 0

    def add(self, item):
        """Adds item to the tree."""

        # Helper function to search for item's position
        def recurse(node):
            # New item is less, go left until spot is found
            if item < node.data:
                if node.left == None:
                    node.left = BSTNode(item)
                else:
                    recurse(node.left)
            # New item is greater or equal,
            # go right until spot is found
            elif node.right == None:
                node.right = BSTNode(item)
            else:
                recurse(node.right)
                # End of recurse

        # Tree is empty, so new item goes at the root
        if self.isEmpty():
            self._root = BSTNode(item)
        # Otherwise, search for the item's spot
        else:
            recurse(self._root)
        self._size += 1

    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item is not in self.
        postcondition: item is removed from self."""
        if not item in self:
            raise KeyError("Item not in tree.""")

        # Helper function to adjust placement of an item
        def lift_max_in_left_subtree_to_top(top):
            """Replace top's datum with the maximum datum in the left subtree
            Pre:  top has a left child
            Post: the maximum node in top's left subtree has been removed
            Post: top.data = maximum value in top's left subtree
            """
            parent = top
            currentnode = top.left
            while not currentnode.right == None:
                parent = currentnode
                currentnode = currentnode.right
            top.data = currentnode.data
            if parent == top:
                top.left = currentnode.left
            else:
                parent.right = currentnode.left

        # Begin main part of the method
        if self.isEmpty(): return None

        # Attempt to locate the node containing the item
        itemremoved = None
        preroot = BSTNode(None)
        preroot.left = self._root
        parent = preroot
        direction = 'L'
        currentnode = self._root
        while not currentnode == None:
            if currentnode.data == item:
                itemremoved = currentnode.data
                break
            parent = currentnode
            if currentnode.data > item:
                direction = 'L'
                currentnode = currentnode.left
            else:
                direction = 'R'
                currentnode = currentnode.right

        # Return None if the item is absent
        if itemremoved == None: return None

        # The item is present, so remove its node

        # Case 1: The node has a left and a right child
        #         Replace the node's value with the maximum value in the
        #         left subtree
        #         Delete the maximium node in the left subtree
        if not currentnode.left == None \
                and not currentnode.right == None:
            lift_max_in_left_subtree_to_top(currentnode)
        else:

            # Case 2: The node has no left child
            if currentnode.left == None:
                newChild = currentnode.right

                # Case 3: The node has no right child
            else:
                newChild = currentnode.left

                # Case 2 & 3: Tie the parent to the new child
            if direction == 'L':
                parent.left = newChild
            else:
                parent.right = newChild

        # All cases: Reset the root (if it hasn't changed no harm done)
        #            Decrement the collection's size counter
        #            Return the item
        self._size -= 1
        if self.isEmpty():
            self._root = None
        else:
            self._root = preroot.left
        return itemremoved

    def replace(self, item, new_item):
        """
        If item is in self, replaces it with new_item and
        returns the old item, or returns None otherwise."""
        probe = self._root
        while probe != None:
            if probe.data == item:
                oldData = probe.data
                probe.data = new_item
                return oldData
            elif probe.data > item:
                probe = probe.left
            else:
                probe = probe.right
        return None

    def height(self):
        """
        Return the height of the tree.
        :return: int
        """
        def height1(top):
            if top is None:
                return 0
            else:
                return 1 + max(height1(top.left), height1(top.right))

        return height1(self._root)-1

    def is_balanced(self):
        """
        Return True if the tree is balanced, False otherwise.
        :return: bool
        """
        def calculate_height(node):
            if node is None:
                return 0
            return 1 + max(calculate_height(node.left), calculate_height(node.right))

        num = self._size
        high = calculate_height(self._root)
        return high <= 2 * log(num + 1, 2) - 1

    def range_find(self, low, high):
        """
        Returns a list of the items in the tree, where low <= item <= high.
        :param low: lower bound of the range
        :param high: upper bound of the range
        :return: list
        """
        def range_find_helper(node, low, high, items):
            if node is None:
                return
            if low <= node.data <= high:
                range_find_helper(node.left, low, high, items)
                items.append(node.data)
                range_find_helper(node.right, low, high, items)
            elif node.data < low:
                range_find_helper(node.right, low, high, items)
            else:
                range_find_helper(node.left, low, high, items)

        items = []
        range_find_helper(self._root, low, high, items)
        return items

    def rebalance(self):
        """
        Rebalances the tree.
        """
        def build_balanced_tree(items):
            if not items:
                return None
            mid = len(items) // 2
            root = BSTNode(items[mid])
            root.left = build_balanced_tree(items[:mid])
            root.right = build_balanced_tree(items[mid + 1:])
            return root

        items = list(self)
        self._root = build_balanced_tree(items)

    def successor(self, item):
        """
        Returns the smallest item that is larger than item, or None if there is no such item.
        :param item: item to find the successor for
        :return: item or None
        """
        def find_successor(node, item, successor):
            if node is None:
                return successor
            if node.data > item:
                successor = node.data
                return find_successor(node.left, item, successor)
            else:
                return find_successor(node.right, item, successor)

        successor = None
        return find_successor(self._root, item, successor)

    def predecessor(self, item):
        """
        Returns the largest element in the tree that is smaller than the given item.
        If there is no such element, returns None.
        """
        def find_predecessor(node, item, predecessor):
            if node is None:
                return predecessor
            if node.data < item:
                predecessor = node.data
                return find_predecessor(node.right, item, predecessor)
            elif node.data >= item:
                return find_predecessor(node.left, item, predecessor)

        predecessor = None
        return find_predecessor(self._root, item, predecessor)
