class LinkedListNode:
    """This is the class of the linked list node"""
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    """This is a linked list class"""
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        curr = self.head
        string = ''
        while curr is not None:
            string += str(curr.value)
            string += ' -> '
            curr = curr.next
        string += 'None'
        return string

    def is_empty(self):
        """Checking if a list is empty"""
        return self.head is None

    def add_last(self, value):
        """Method for adding a node to the end of the list"""
        node = LinkedListNode(value)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def add_first(self, value):
        """Method for adding a node to the beginning of the list"""
        node = LinkedListNode(value)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node

    def __len__(self):
        if self.is_empty():
            return 0
        current, ind = self.head, 0
        while current is not None:
            current = current.next
            ind += 1
        return ind

    def insert(self, index_node, value):
        """Method for inserting a node with a specified value
        at a specified index into a list"""
        if index_node == 0:
            self.add_first(value)
        elif index_node == len(self):
            self.add_last(value)
        elif 0 < index_node < len(self):
            node = LinkedListNode(value)
            count = 0
            current = self.head
            while current:
                if index_node == count + 1:
                    node.next = current.next
                    current.next = node
                current = current.next
                count += 1

    def search(self, index_node):
        """The method will return the value of the node at the given index"""
        if self.is_empty():
            print("List is empty")
        current = self.head
        count = 0
        while count <= index_node:
            if count == index_node:
                return current.value
            count += 1
            current = current.next

    def remove_node(self, index_node):
        """Method for removing a node at a given index from the list"""
        if index_node < 0:
            raise ValueError("Value must be positive")
        if self.is_empty():
            print("List is empty")
        else:
            current = self.head
            prev = None
            index = 0
            while index <= index_node:
                if index == index_node:
                    if current == self.head:
                        self.head = current.next
                    else:
                        prev.next = current.next
                    break
                index += 1
                prev = current
                current = current.next

