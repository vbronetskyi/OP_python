"""
Stack to queue converter.
"""
from arrayqueue import ArrayQueue    # or from linkedqueue import LinkedQueue
from linkedstack import LinkedStack    # or from linkedstack import LinkedStack
def stack_to_queue(stack):
    """func"""
    queue = ArrayQueue()
    temp_stack = LinkedStack(stack)
    while not temp_stack.isEmpty():
        queue.add(temp_stack.pop())
    return queue

stack = LinkedStack()
for i in range(10):
        stack.add(i)
queue = stack_to_queue(stack)
print(queue)
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(stack)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(stack.pop())
# 9
print(queue.pop())
# 9
stack.add(11)
queue.add(11)
print(queue)
# [8, 7, 6, 5, 4, 3, 2, 1, 0, 11]
print(stack)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 11]
