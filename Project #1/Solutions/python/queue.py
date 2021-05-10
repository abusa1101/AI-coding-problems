""" Queue Classes Used to Order General Search Code Open List"""

from collections import deque



class Queue:
    """ FIFO Queue class """
    def __init__(self):
        self.queue = deque()

    def push(self, item):
        """ Push items onto queue """
        self.queue.append(item)

    def pop(self):
        """ Pop items off of queue """
        return self.queue.popleft()

    def is_empty(self):
        """ empty check """
        return self.size() == 0

    def size(self):
        """ returns size of queue """
        return len(self.queue)


class Stack(Queue):
    """ LIFO Queue class """
    def pop(self):
        return self.queue.pop()


class PriorityQueue(Queue):
    """ Priority Queue class """
    def pop(self):
        """ pop items from priority Queue """
        min_item = min(self.queue)
        self.queue.remove(min_item)
        return min_item



def test_queues():
    """ Testing Queue Classes """
    print("Testing Queue Classes!")

    # 1) Test FIFO Queue
    print("\n       FIFO Queue")
    in_vals = [2, 0, 3, 1, 5]
    out_vals = []
    my_q = Queue()
    for val in in_vals:
        my_q.push(val)
    while not my_q.is_empty():
        out_vals.append(my_q.pop())
    print("Input  - ", in_vals)
    print("Output - ", out_vals)

    # 2) Test LIFO Stack
    print("\n       LIFO Stack")
    in_vals = [2, 0, 3, 1, 5]
    out_vals = []
    my_q = Stack()
    for val in in_vals:
        my_q.push(val)
    while not my_q.is_empty():
        out_vals.append(my_q.pop())
    print("Input  - ", in_vals)
    print("Output - ", out_vals)


    # 3) Test Priority Queue
    print("\n       Priority Queue")
    in_vals = [2, 0, 3, 1, 5]
    out_vals = []
    my_q = PriorityQueue()
    for val in in_vals:
        my_q.push(val)
    while not my_q.is_empty():
        out_vals.append(my_q.pop())
    print("Input  - ", in_vals)
    print("Output - ", out_vals)

if __name__ == "__main__":
    test_queues()
