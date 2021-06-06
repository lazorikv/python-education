import pytest
from queue import Queue
from random import randint


@pytest.fixture
def some_queue():
    queue = Queue()
    python_list = []
    for i in range(50):
        value = randint(0, 50)
        queue.enqueue(value)
        python_list.append(value)

    return queue, python_list


def test_empty():
    """Testing function isEmpty"""
    queue = Queue()
    assert queue.isEmpty() is True


def test_enqueue():
    """Testing function enqueue"""
    queue = Queue()
    python_list = []
    for i in range(50):
        value = randint(0, 50)
        queue.enqueue(value)
        python_list.insert(0, value)
    assert queue.peek_last() == python_list[0]


def test_dequeue(some_queue):
    """Testing function dequeue"""
    queue, python_list = some_queue
    queue.dequeue()
    assert queue.peek() == python_list[1]


def test_peek(some_queue):
    """Testing function peek"""
    queue, python_list = some_queue
    peek_q = queue.peek()
    peek_l = python_list[0]
    assert peek_q == peek_l


def test_peek_last(some_queue):
    """Testing function peek_last"""
    queue, python_list = some_queue
    peek_q = queue.peek_last()
    peek_l = python_list[-1]
    assert peek_q == peek_l



