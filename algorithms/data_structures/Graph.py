"""Module to represent Graph"""


from LinkedList import LinkedList


class LinkedListGraph(LinkedList):
    """A linked list class for a graph"""
    def __init__(self):
        super().__init__()

    def delete_edge_vertex(self, value):
        """Method of removing all edges that contain
        a vertex with a specified value"""
        if self.is_empty():
            print("Список пуст")
        else:
            current = self.head
            ind = 0

            while current is not None:
                if value in current.value:
                    self.remove_node(ind)
                else:
                    ind += 1
                current = current.next


class Graph:
    """Class realized methods for Graph"""
    def __init__(self):
        self.vertex = LinkedListGraph()
        self.edges = LinkedListGraph()

    def __str__(self):
        current_vertex = self.vertex.head
        string = ''
        while current_vertex is not None:
            string += str(current_vertex.value)
            string += ' -> '
            current_vertex = current_vertex.next
        string += 'None\n'

        current_edge = self.edges.head
        while current_edge is not None:
            string += str(current_edge.value)
            string += ' -> '
            current_edge = current_edge.next
        string += 'None'
        return string

    def edge_exists(self, vertex1, vertex2):
        """Method for checking the existence of an edge"""
        return self.edges.is_value((vertex1, vertex2))

    def vertex_exists(self, value):
        """Method for checking the existence of an vertex"""
        return self.vertex.is_value(value)

    def add_edge(self, vertex1, vertex2):
        """Edge adding method"""
        if self.edges.is_empty() or not self.edge_exists(vertex1, vertex2):
            self.edges.add_last((vertex1, vertex2))
        else:
            raise ValueError("That edge is exists")

    def add_vertex(self, value):
        """Method for add vertex"""
        if self.vertex.is_empty() or not self.vertex_exists(value):
            self.vertex.add_last(value)
        else:
            raise ValueError("That vertex is exists")

    def delete_vertex(self, value):
        """Method for delete vertex"""
        if self.vertex_exists(value):
            self.edges.delete_edge_vertex(value)
            self.vertex.remove_node(value)
        else:
            raise ValueError("No such vertex exists")

    def get_vertex(self, index):
        return self.vertex.search(index)

    def get_edge(self, index):
        return self.edges.search(index)




