"""Module to represent Graph"""


class Graph:

    def __init__(self, graph_dict=None):
        """ initializes a graph object
            If no dictionary or None is given,
            an empty dictionary will be used"""

        if graph_dict is None:
            graph_dict = {}
        self.graph_dict = graph_dict

    def edges(self, e_vertex):
        """returns a list of all the edges of a vertex"""
        return self.graph_dict[e_vertex]

    def all_vertices(self):
        """ returns the vertices of a graph as a set"""
        return set(self.graph_dict.keys())

    def all_edges(self):
        """ returns the edges of a graph """
        return self.generate_edges()

    def add_vertex(self, vertex):
        """ If the vertex is not in
            self.graph_dict, a key "vertex" with an empty
            list as a value is added to the dictionary.
            Otherwise nothing has to be done"""
        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = []

    def add_edge(self, edge):
        """ assumes that edge is of type set, tuple or list;
            between two vertices can be multiple edges!"""
        edge = set(edge)
        vertex1, vertex2 = tuple(edge)
        for x, y in [(vertex1, vertex2), (vertex2, vertex1)]:
            if x in self.graph_dict:
                self.graph_dict[x].add(y)
            else:
                self.graph_dict[x] = [y]

    def generate_edges(self):
        """A method generating the edges of the graph """
        edges = []
        for vertex in self.graph_dict:
            for neighbour in self.graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def __iter__(self):
        self.iter_obj = iter(self.graph_dict)
        return self.iter_obj

    def __next__(self):
        """ allows us to iterate over the vertices """
        return next(self.iter_obj)

    def __str__(self):
        res = "vertices: "
        for k in self.graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.generate_edges():
            res += str(edge) + " "
        return res


g = { "a": {"d"},
      "b": {"c"},
      "c": {"b", "c", "d", "e"},
      "d": {"a", "c"},
      "e": {"c"},
      "f": {}
    }

graph = Graph(g)

for vertex in graph:
    print(f"Edges of vertices {vertex}: ", graph.edges(vertex))
