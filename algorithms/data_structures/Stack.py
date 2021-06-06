"""Module to represent Stack"""


class Node:
    """class to represent each node of the Stack"""
    def __init__(self, elem):
        self.elem = elem
        self.next = None

    def __repr__(self):
        return self.elem


class Stack:
    """Class realized methods for Stack"""
    def __init__(self):
        self.head = None

    def __str__(self):
        s = ''
        current = self.head
        while current is not None:
            s += str(current.elem) + ' '
            current = current.next
        return s

    def custom_push(self, elem):
        """Method push data to class Stack"""
        if self.head is None:
            self.head = Node(elem)
        else:
            new_node = Node(elem)
            new_node.next = self.head
            self.head = new_node

    def custom_pop(self):
        """Method pop data to class Stack"""
        if self.head is None:
            return None
        else:
            popped = self.head.elem
            self.head = self.head.next
            return popped

    def custom_peek(self):
        """Shows peek of the stack"""
        return self.head.elem


stack = Stack()
stack.custom_push(Node('oleg'))
stack.custom_push(Node('igor'))
stack.custom_push(Node('egor'))
print(stack)
stack.custom_pop()
print(stack)
print(stack.custom_peek())
