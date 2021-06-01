"""Testing module 'quick_sort'"""

import quick_sort
import random

#  random filling of a list
random_list = []
for elem in range(5):
    random_list.append(random.randint(0, 50))
expected_list = random_list[:]


def test_quick_sort():
    """
    Comparison of custom quick sort with built-in sorting tool
    """
    n = len(random_list)-1
    test_sorting = quick_sort.QuickSort()
    test_sorting.quickSort(random_list, 0, n)
    a = sorted(expected_list)
    assert random_list == a
