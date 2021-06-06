import pytest
from LinkedList import LinkedList
from random import randint


def test_a_l():
    """Testing function add_last"""
    python_list = []
    list_1 = LinkedList()
    for i in range(100):
        value = randint(0, 50)
        list_1.add_last(value)
        python_list.append(value)
    for i in range(100):
        assert list_1.search(i) == python_list[i]


def test_a_f():
    """Testing function add_first"""
    python_list = []
    list_2 = LinkedList()
    for i in range(100):
        value = randint(0, 50)
        list_2.add_first(value)
        python_list.insert(0, value)
    for i in range(100):
        assert list_2.search(i) == python_list[i]


def test_insert():
    """Testing function insert"""
    python_list = []
    list_3 = LinkedList()
    for i in range(100):
        value = randint(0, 50)
        python_list.insert(i, value)
        list_3.insert(i, value)
        assert list_3.search(i) == python_list[i]


def test_search():
    """Testing function insert"""
    python_list = []
    list_4 = LinkedList()
    for i in range(100):
        value = randint(0, 50)
        python_list.insert(i, value)
        list_4.insert(i, value)
    assert list_4.search(5) == python_list[5]


def test_remove():
    """Testing function delete_node"""
    python_list = []
    list_4 = LinkedList()
    for i in range(100):
        value = randint(0, 50)
        python_list.insert(i, value)
        list_4.insert(i, value)
    list_4.remove_node(0)
    python_list = python_list[1:]
    for i in range(99):
        assert list_4.search(i) == python_list[i]