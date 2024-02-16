"""
Queue to stack converter.
"""
from arrayqueue import ArrayQueue
from arraystack import ArrayStack
import copy
def queue_to_stack(queue):
    """queue_to_stack"""
    stack = ArrayStack()
    queue = copy.deepcopy(queue)

    while not queue.isEmpty():
        stack.push(queue.remove(len(queue) - 2 + 1))
    return stack

# queue = ArrayQueue()
# for i in range(10):
#     queue.add(i)
# stack = queue_to_stack(queue)
# print(queue)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(stack)  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
# print(stack.pop())  # 0
# print(queue.pop())  # 0
# stack.add(11)
# queue.add(11)
# print(queue)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 11]
# print(stack)  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 11]
