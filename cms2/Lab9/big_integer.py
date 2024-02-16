"""integer"""
VARIANT = 22
class Node:
    """Node"""
    def __init__(self, val=0, prev=None, next=None):
        """__init__"""
        self.val = val
        self.prev = prev
        self.next = next

class BigInteger:
    """BigInteger"""
    def __init__(self, initValue="0"):
        """__init__"""
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

        for digit in reversed(initValue):
            self.add_digit(int(digit))

    def add_digit(self, digit):
        """додаємо новий вузол з цифрою на початок списку"""
        new_node = Node(digit, self.head, self.head.next)
        self.head.next.prev = new_node
        self.head.next = new_node

    def remove_leading_zeroes(self):
        """видаляємо нульові значущі цифри з початку числа"""
        while self.tail.prev != self.head and self.tail.prev.val == 0:
            self.tail.prev = self.tail.prev.prev
            self.tail.prev.next = self.tail

    def to_string(self):
        """повертаємо число у вигляді рядка"""
        self.remove_leading_zeroes()
        digits = []
        cur_node = self.head.next
        while cur_node != self.tail:
            digits.append(str(cur_node.val))
            cur_node = cur_node.next
        if not digits:
            digits.append('0')
        return ''.join(reversed(digits))

    def __lt__(self, other):
        """__lt__"""
        return int(self.to_string()) < int(other.to_string())

    def __eq__(self, other):
        """__eq__"""
        return int(self.to_string()) == int(other.to_string())

    def __pow__(self, other):
        """піднесення до степеню за допомогою алгоритму бінарного піднесення до степеню"""
        result = BigInteger("1")
        base = BigInteger(self.to_string())
        while other > 0:
            if other % 2 == 1:
                result *= base
            base *= base
            other //= 2
        return result

    def __mod__(self, other):
        """реалізація операції %"""
        quotient, remainder = self.divmod(other)
        return remainder

    def __rshift__(self, other):
        """реалізація операції >>"""
        result = BigInteger(self.to_string())
        for _ in range(other):
            result.remove_leading_zeroes()
            result.tail.prev = result.tail.prev.prev
            result.tail.prev.next = result.tail
        return result

    def __and__(self, other):
        """реалізація операції &"""
        result = BigInteger()
        self_node = self.tail.prev
        other_node = other.tail.prev
        while self_node != self.head and other_node != other.head:
            result.add_digit(self_node.val & other_node.val)
            self_node = self_node.prev
            other_node = other_node.prev
        return result
