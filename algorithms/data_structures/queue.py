"""Module to represent Queue"""


class Node:
    """class to represent each node of the queue"""
    def __init__(self, item):
        self.item = item  # Reference to an item
        self.next = None  # Reference to the next _Node object

    def __repr__(self):
        return self.item


class Queue:
    """Class realized methods for Queue"""
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def __str__(self):
        s = ''
        current = self.first
        while current is not None:
            s += str(current.item) + ' '
            current = current.next
        return s

    def isEmpty(self) -> None:
        return self.first is None

    def __len__(self) -> int:
        """Length of queue"""
        return self.size

    def enqueue(self, item):
        """Add item to the end of self"""
        node = Node(item)
        if self.isEmpty():
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node

    def dequeue(self):
        """Remove the first item of self and return it"""
        if self.isEmpty():
            print("Queue is empty")
        else:
            self.first = self.first.next
        # item = self.first.item
        # self.first = self.first.next
        # if self.isEmpty():
        #     self.last = None
        # self.size -= 1
        # return item

    def peek(self):
        """Shows peek of the queue"""
        return self.first.item

    def peek_last(self):
        """Shows last peek of the queue"""
        return self.last.item


some_queue = Queue()
some_queue.enqueue(Node('r'))
some_queue.enqueue(Node('sdvs'))
some_queue.enqueue(Node('tert'))
print(some_queue)
some_queue.dequeue()
print(some_queue)
print(some_queue.peek())


