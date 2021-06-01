"""Testing module 'binary_search'"""

from binary_search import BinarySearch
from quick_sort import QuickSort
import pytest


@pytest.mark.parametrize('test_args, expected', [([12, 6, 3, 9, 4, 7, 4], 6),
                                                 ([-3, 5, 2, 4, 12, 15, 7], 5),
                                                 ([3, 12, 5, 18, 19, 10], 3)])
def test_bin_search(test_args, expected):
    """The list is first sorted with a custom quick search,
    then a binary search occurs
    param: n - Length of entered list (int)
    param: b_search - result of binary search
    """
    print(test_args)
    n = len(test_args) - 1
    test_sort = QuickSort()
    test_sort.quickSort(test_args, 0, n)
    b_search = BinarySearch().bin_search(test_args, 12)
    assert b_search == expected
