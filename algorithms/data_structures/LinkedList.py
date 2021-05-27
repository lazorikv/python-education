"""Module to represent LinkedList"""


class Node:
    """class to represent each node of the linked list"""
    def __init__(self, elem=None):
        self.elem = elem
        self.next = None

    def __repr__(self):
        return self.elem


class LinkedList:
    """Class realized methods for LinkedList"""
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(elem=nodes.pop(0))
            self.head = node
            for data in nodes:
                node.next = Node(elem=data)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.elem)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        """traverse linkedlist"""
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_first(self, node):
        """Insert element to begin of linkedlist"""
        node.next = self.head
        self.head = node

    def add_last(self, node):
        """Insert element to end of linkedlist"""
        if self.head is None:
            self.head = node
            return
        for this_node in self:
            pass
        this_node.next = node

    def search(self, get_elem: int) -> int:
        """item search by index"""
        if isinstance(get_elem, int):
            current = self.head
            count = 0
            while count != get_elem:
                current = current.next
                count += 1
            return current.elem
        else:
            raise ValueError

    def remove_node(self, target_node_elem):
        """Remove element from linkedlist"""
        if self.head.elem == target_node_elem:
            self.head = self.head.next
            return

        prev_node = self.head
        for node in self:
            if node.elem == target_node_elem:
                prev_node.next = node.next
                return
            prev_node = node

        if self.head is None:
            raise Exception("List is empty")
        raise Exception("Node with data '%s' not found" % target_node_elem)


llist = LinkedList()
first = Node('a')
second = Node('b')
zero = Node('0')
llist.head = first
first.next = second
llist.add_first(zero)
some_llist = LinkedList(["a", "b", "c", "d", "e"])
for elem in some_llist:
    print(elem)
llist.add_last(Node('p'))
print(f'Index 3 - {some_llist.search(3)}')
some_llist.remove_node('a')
print(llist)
print(some_llist)
