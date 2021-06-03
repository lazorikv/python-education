"""Module to represent Tree"""


class Node:
    """This is the class of the linked list node"""

    def __init__(self, key, value) -> None:
        self.value = value
        self.index = None
        self.key = key
        self.next = None


class Hashtable:
    """Class realized methods for Stack"""

    def __init__(self) -> None:
        self.head = None

    @staticmethod
    def hash(key):
        """Hash-function"""
        if isinstance(key, int):
            return key % 256
        else:
            mass_of_string = 0
            for pos, val in enumerate(key):
                mass_of_string = mass_of_string + ord(key[pos])
            return mass_of_string % 256

    def add_item(self, key, value):
        """insert a pair of key and value into a hash table"""
        if self.head is None:
            self.head = Node(key, value)
            self.head.index = self.hash(key)
            return

        curr_node = self.head
        while curr_node.next is not None:
            if curr_node.next.index == self.hash(key):
                curr_node.next.value = Node(key, value).value
                return
            else:
                curr_node = curr_node.next

        curr_node.next = Node(key, value)
        curr_node.next.index = self.hash(key)

    def find(self, key):
        """Find data from hash table"""
        curr_node = self.head
        counter = 0
        while curr_node.next is not None:
            if self.hash(key) == curr_node.index:
                return curr_node.value
            curr_node = curr_node.next
            counter += 1
        print(f"Key {key} not found")
        return

    def remove(self, key):
        """Remove data from hash table"""
        rem_item = self.find(key)
        prev_node = None
        curr_node = self.head
        next_node = curr_node.next
        count = 0
        while curr_node.next is not None:
            if rem_item == curr_node.value:
                break
            prev_node = curr_node
            curr_node = prev_node.next
            next_node = curr_node.next
            count += 1

        prev_node.next = next_node
        next_node = prev_node.next

    def print_table(self):
        """Print pair of key and value from hash-table"""
        curr_node = self.head
        while curr_node.next is not None:
            print(f"{curr_node.key} -> {curr_node.value}")
            curr_node = curr_node.next
        print(f"{curr_node.key} -> {curr_node.value}")


ht = Hashtable()
ht.add_item('ukraine', 'kharkiv')
ht.add_item('ukraine', 'kiev')
ht.add_item('poland', 'wroclav')
ht.add_item('belarussia', 'Minsk')
ht.add_item('belarussia', 'grodno')
ht.print_table()
ht.remove('poland')
ht.print_table()
