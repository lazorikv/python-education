"""This module to implement a hash table"""

from LinkedList import LinkedList


class LinkedListHash(LinkedList):
    """Custom linkedlist for hash table"""

    def is_value(self, key):
        """Method for checking the existence of
        a node with a given value in the list"""
        current = self.head
        while current is not None:
            if current.value[0] == key:
                return current.value[1]
            current = current.next
        return None


class HashTable:
    """Class implements hashtable with linkedlist"""
    def __init__(self):
        self.size = 6
        self.table = [LinkedListHash() for _ in range(self.size)]

    def hash(self, string):
        """Method implements hashing the data"""
        return sum(ord(item) for item in string) % self.size

    def __getitem__(self, string):
        """Find data from hash table"""
        return self.table[self.hash(string)].is_value(string)

    def __setitem__(self, string, value):
        """Add data to the hashtable"""
        if self[string] is None:
            self.table[self.hash(string)].add_last((string, value))

    def print_table(self):
        """Print hashtable"""
        for elem in self.table:
            print(str(elem))


ht = HashTable()
ht["Oleg"] = 1
ht["Vova"] = 2
ht["Igor"] = 23
print(ht.hash("Igor"))
ht.print_table()
