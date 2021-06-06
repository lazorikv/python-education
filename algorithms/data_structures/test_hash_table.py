"""Test module for Hash Table"""

import pytest
from HashTable import Hashtable


@pytest.fixture
def some_hash_table():
    return Hashtable()


@pytest.fixture
def find():
    ht = Hashtable()
    ht.add_item('Turkey', 'istambul')
    ht.add_item('ukraine', 'kharkiv')
    ht.add_item('poland', 'wroclav')
    ht.add_item('belarussia', 'Minsk')
    ht.add_item('belarussia', 'grodno')
    return ht


@pytest.mark.parametrize('testing, expected', [(543, 31),
                                               ('elephant', 81),
                                               ('tiger', 27)])
def test_hash(some_hash_table, testing, expected):
    """Testing function hash"""
    assert some_hash_table.hash(testing) == expected


def test_add_item(some_hash_table):
    """Testing function add_item"""
    some_hash_table.add_item('Germany', 'Berlin')
    assert some_hash_table.head.value == 'Berlin'
    assert some_hash_table.head.key == 'Germany'
    assert some_hash_table.head.index is not None
    assert some_hash_table.head.next is None
    some_hash_table.add_item('belarussia', 'Minsk')
    assert some_hash_table.head.next is not None


def test_find(find):
    """Testing function find"""
    assert find.find('poland') == 'wroclav'


def test_remove(find):
    """Testing function remove"""
    assert find.head.next.key == 'ukraine'
    find.remove('ukraine')
    assert find.head.next.key == 'poland'
