"""Module to represent HashTable"""


class Node:
    """class to represent each node of the Stack"""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """Class realized methods for Stack"""
    def __init__(self):
        self.capacity = 30
        self.size = 0
        self.buckets = [None] * self.capacity

    def hash(self, key) -> int:
        """Hash-function"""
        hashsum = 0
        for index, c in enumerate(key):
            hashsum += (index + len(key)) ** ord(c)
            hashsum = hashsum % self.capacity
        return hashsum

    def insert(self, key, value):
        """insert a pair of key and value into a hash table"""
        self.size += 1
        index = self.hash(key)
        node = self.buckets[index]

        if node is None:
            self.buckets[index] = Node(key, value)
            return

        prev = node
        while node is not None:
            prev = node
            node = node.next
        prev.next = Node(key, value)

    def find(self, key):
        """Find data from hash table"""
        index = self.hash(key)
        node = self.buckets[index]
        while node is not None and node.key != key:
            node = node.next
        if node is None:
            return None
        else:
            return node.value

    def remove(self, key):
        """Remove data from hash table"""
        index = self.hash(key)
        node = self.buckets[index]
        prev = None
        while node is not None and node.key != key:
            prev = node
            node = node.next

        if node is None:
            return None
        else:
            self.size -= 1
            result = node.value
            if prev is None:
                node = None
            else:
                prev.next = prev.next.next
            return result


ht = HashTable()
phone_numbers = ['0508494944', '05056698489']
ht.insert("myphonedirectory", phone_numbers)
phone_numbers = ht.find("myphonedirectory")
print(phone_numbers)



