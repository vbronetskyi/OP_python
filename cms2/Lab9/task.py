VARIANT = 22
class Node:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class BigInteger:
    def __init__(self, initValue="0"):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

        # розбиваємо поцифрово введене значення та додаємо його до списку
        for digit in reversed(initValue):
            self.add_digit(int(digit))

    def add_digit(self, digit):
        # додаємо новий вузол з цифрою на початок списку
        new_node = Node(digit, self.head, self.head.next)
        self.head.next.prev = new_node
        self.head.next = new_node

    def remove_leading_zeroes(self):
        # видаляємо нульові значущі цифри з початку числа
        while self.tail.prev != self.head and self.tail.prev.val == 0:
            self.tail.prev = self.tail.prev.prev
            self.tail.prev.next = self.tail

    def to_string(self):
        # повертаємо число у вигляді рядка
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
        return int(self.to_string()) < int(other.to_string())

    def __eq__(self, other):
        return int(self.to_string()) == int(other.to_string())

    def __pow__(self, other):
        # піднесення до степеню за допомогою алгоритму бінарного піднесення до степеню
        result = BigInteger("1")
        base = BigInteger(self.to_string())
        while other > 0:
            if other % 2 == 1:
                result *= base
            base *= base
            other //= 2
        return result

    def __mod__(self, other):
        # реалізація операції %
        quotient, remainder = self.divmod(other)
        return remainder

    def __rshift__(self, other):
        # реалізація операції >>
        result = BigInteger(self.to_string())
        for i in range(other):
            result = result.floordiv(BigInteger("2"))
        return result

    def __lshift__(self, other):
        # реалізація операції <<
        result = BigInteger(self.to_string())
        for i in range(other):
            result = result.mul(BigInteger("2"))
        return result

    def __and__(self, other):
        # реалізація операції &
        result = BigInteger()
        cur_node_self = self.tail.prev
        cur_node_other = other.tail.prev
        while cur_node_self != self.head and cur_node_other != other.head:
            result.add_digit(cur_node_self.val & cur_node_other.val)
            cur_node_self = cur_node_self.prev
            cur_node_other = cur_node_other.prev
        return result

    def __or__(self, other):
        # реалізація операції |
        result = BigInteger()
        cur_node_self = self.tail.prev
        cur_node_other = other.tail.prev
        while cur_node_self != self.head or cur_node_other != other.head:
            result.add_digit(cur_node_self.val | cur_node_other.val)
            if cur_node_self.prev:
                cur_node_self = cur_node_self.prev
            if cur_node_other.prev:
                cur_node_other = cur_node_other.prev
        return result

    def __xor__(self, other):
        # реалізація операції ^
        result = BigInteger()
        cur_node_self = self.tail.prev
        cur_node_other = other.tail.prev
        while cur_node_self != self.head or cur_node_other != other.head:
            result.add_digit(cur_node_self.val ^ cur_node_other.val)
            if cur_node_self.prev:
                cur_node_self = cur_node_self.prev
            if cur_node_other.prev:
                cur_node_other = cur_node_other.prev
        return result

    def add(self, other):
        # реалізація операції +
        result = BigInteger()
        carry = 0
        cur_node_self = self.tail.prev
        cur_node_other = other.tail.prev
        while cur_node_self != self.head or cur_node_other != other.head or carry:
            a = cur_node_self.val if cur_node_self != self.head else 0
            b = cur_node_other.val if cur_node_other != other.head else 0
            s = a + b + carry
            carry = s // 10
            result.add_digit(s % 10)
            if cur_node_self.prev:
                cur_node_self = cur_node_self.prev
            if cur_node_other.prev:
                cur_node_other = cur_node_other.prev
        return result

    def sub(self, other):
        # реалізація операції -
        result = BigInteger()
        borrow = 0
        cur_node_self = self.tail.prev
        cur_node_other = other.tail.prev
        while cur_node_self != self.head or cur_node_other != other.head or borrow:
            a = cur_node_self.val if cur_node_self != self.head else 0
            b = cur_node_other.val if cur_node_other != other.head else 0
            d = a - b - borrow
            if d < 0:
                d += 10
                borrow = 1
