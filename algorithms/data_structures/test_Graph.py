"""Test module for Graph"""

import itertools
from Graph import Graph
import pytest


@pytest.fixture
def some_graph():
    graph = Graph()
    python_list = []
    return graph, python_list


def test_add_vertex(some_graph):
    """Testing function add_vertex"""
    graph, python_list = some_graph
    for i in range(50):
        graph.add_vertex(i)
        python_list.append(i)
        assert graph.get_vertex(i) == python_list[i]


def test_add_edge(some_graph):
    """Texting function add_edge"""
    vertex_1 = []
    vertex_2 = []
    graph, python_list = some_graph
    for i in range(10):
        vertex_1.append(i)
    for i in range(11, 50):
        vertex_2.append(i)

    vertex = [vertex_1, vertex_2]
    for elem in itertools.product(*vertex):
        graph.add_edge(*elem)
        python_list.append(elem)

    for i in range(len(python_list)):
        assert graph.get_edge(i) == python_list[i]
