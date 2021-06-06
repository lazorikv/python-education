"""Test module for stack"""

import pytest
from Stack import Stack
from random import randint


@pytest.fixture
def some_stack():
    stack = Stack()
    python_list = []
    for i in range(50):
        value = randint(0, 50)
        stack.custom_push(value)
        python_list.append(value)
    python_list = python_list[::-1]
    return stack, python_list


def test_custom_push(some_stack):
    """Testing function custom_push"""
    stack, python_list = some_stack
    assert stack.custom_peek() == python_list[0]


def test_custom_peek(some_stack):
    """Testing function custom_peek"""
    stack, python_list = some_stack
    assert stack.custom_peek() == python_list[0]


def test_custom_pop(some_stack):
    """Testing function custom_pop"""
    stack, python_list = some_stack
    for i in range(50):
        assert stack.custom_pop() == python_list[i]