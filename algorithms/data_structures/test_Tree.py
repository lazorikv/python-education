"""Test module for Tree"""

import pytest
from Tree import Tree


@pytest.fixture
def test_tree():
    some_tree = Tree()
    return some_tree


@pytest.mark.parametrize('test_arg',
                         [
                             ([100, 200, 300, 400, 350, 250, 880])
                         ])
def test_tree_init(test_tree, test_arg):
    """Testing module Tree"""
    tree = test_tree
    right_side = max(test_arg)
    root = tree.insert(None, test_arg[0])

    for i in range(1, len(test_arg)):
        tree.insert(root, test_arg[i])
    root_curr = root

    while root_curr is not None:
        root_curr = root_curr.right
        if root_curr.right is None:
            break

    assert root_curr.data == right_side
