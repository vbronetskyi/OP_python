"""multiset"""
from node import *

# A class implementing Multiset as a linked list.

class Multiset:
    """A class implementing Multiset as a linked list."""
    def __init__(self):
        """
        Produces a newly constructed empty Multiset.
        __init__: -> Multiset
        Field: _head points to the first node in the linked list
        """
        self._head = None

    def empty(self):
        """
        Checks emptiness of Multiset.
        empty: Multiset -> Bool
        :return: True if Multiset is empty and False otherwise.
        """
        return self._head == None

    def __contains__(self, value):
        """
        Checks existence of value in the Multiset.
        __contains__: Multiset Any -> Bool
        :param value: the value to be check.
        :return: True if Multiset is in the Multiset and False otherwise.
        """
        current = self._head
        while current != None:
            if current.item == value:
                return True
            else:
                current = current.next
        return False

    def add(self, value):
        """
        Adds the value to multiset.

        :param value: the value to be added.
        """
        if self._head is None:
            self._head = Node(value)
        else:
            rest = self._head
            self._head = Node(value)
            self._head.next = rest

    def delete(self, value):
        """
        :param value: value first occurrence of which should be deleted.
        """
        current = self._head
        previous = None
        while current is not None and current.item != value:
            previous = current
            current = current.next
        if current is not None:
            if previous is None:
                self._head = self._head.next
            else:
                previous.next = current.next
    def remove_all(self):
        """remove_all elemen"""
        if self._head is None:
            return []
        result = []
        while self._head is not None:
            result.append(self._head.item)
            self._head = self._head.next
        return result

    def split_half(self):
        """split_half"""
        if self._head is None:
            return None, None
        current = self._head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        current = self._head
        half_count = count // 2 + count % 2
        for _ in range(1, half_count):
            current = current.next
        head2 = current.next
        current.next = None
        return self._head, head2

    def extend(self, other):
        """extend"""
        if other is None or other.empty():
            return self
        if self.empty():
            self._head = other._head
            return self
        current = other._head
        while current.next is not None:
            current = current.next
        current.next = self._head
        return other


multiset_1 = Multiset()
multiset_2 = Multiset()
multiset_1.add('p')
multiset_1.add('y')
multiset_1.add('t')
multiset_2.add('h')
multiset_2.add('o')
multiset_2.add('n')
print(multiset_1.extend(multiset_2).remove_all())
# ['n', 'o', 'h', 't', 'y', 'p']
