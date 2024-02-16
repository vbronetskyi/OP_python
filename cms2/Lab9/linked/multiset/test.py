from node import *

class Multiset:
    def __init__(self):
        self._head = None

    def empty(self):
        return self._head is None

    def __contains__(self, value):
        current = self._head
        while current is not None:
            if current.item == value:
                return True
            else:
                current = current.next
        return False

    def add(self, value):
        if self._head is None:
            self._head = Node(value)
        else:
            current = self._head
            while current.next is not None:
                current = current.next
            current.next = Node(value)

    def delete(self, value):
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

    def remove_all(self, head=None):
        result = []
        current = head or self._head
        while current is not None:
            result.append(current.item)
            current = current.next
            if head is None:
                self._head = None
        return result[::-1]

    def split_half(self):
        if self._head is None:
            return None, None

        slow = self._head
        fast = self._head.next

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        second_half = slow.next
        slow.next = None

        return self._head, second_half

    def extend(self, multiset):
        if self._head is None:
            return multiset

        current = self._head
        while current.next is not None:
            current = current.next

        current.next = multiset._head

        return self
multiset_1 = Multiset()
multiset_2 = Multiset()
multiset_1.add('p')
multiset_1.add('y')
multiset_1.add('t')
multiset_2.add('h')
multiset_2.add('o')
multiset_2.add('n')
print(multiset_1.extend(multiset_2).remove_all())