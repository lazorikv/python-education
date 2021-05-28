"""
Module implements binary search for an element in list
Using custom method for quick sort of list
"""


import quick_sort


class BinarySearch:
    """Implements binary search for an element in list"""
    def __init__(self):
        """
        param: _low - starting boundary value
        """
        self._low = 0

    def bin_search(self, some_list: list, x) -> int:
        """
        Binary search for an element in list

        Parameters

        some_list - entered list
        x - searching value
        high - starting boundary value
        middle - Average value between borders
        """
        high = len(some_list) - 1
        while self._low <= high:
            middle = self._low + (high - self._low)//2
            if some_list[middle] == x:
                return middle
            elif some_list[middle] < x:
                self._low = middle + 1
            else:
                high = middle - 1
        return -1


def main():
    test_list = [2, 15, 3, 144, 12, 17, 6, 9, 1]
    n = len(test_list) - 1
    quick_sort.QuickSort().quickSort(test_list, 0, n)
    print(test_list)
    print(BinarySearch().bin_search(test_list, 12))


if __name__ == '__main__':
    main()
