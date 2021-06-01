"""A module that implements Quick Sort"""
import random


class QuickSort:

    @staticmethod
    def splitter(array: list, low: int, high: int) -> int:
        """A function that splits an array

        Parameters

        low - starting boundary value
        high - starting boundary value
        array - entered list

        """
        i = low-1
        change = array[high]  # pivot element
        for j in range(low, high):
            if array[j] <= change:
                i = i+1
                array[i], array[j] = array[j], array[i]
        array[i+1], array[high] = array[high], array[i+1]
        return i+1

    def quickSort(self, array, low, high) -> None:
        """Main function of sorting"""
        if low < high:
            pi = self.splitter(array, low, high)
            self.quickSort(array, low, pi-1)
            self.quickSort(array, pi+1, high)


def main():
    some_list = []
    for i in range(10):
        some_list.append(random.randint(0, 50))
    size = len(some_list)-1
    print(some_list)
    sorting = QuickSort()
    sorting.quickSort(some_list, 0, size)
    print("Sorted array: ")
    for i in range(size+1):
        print(some_list[i], end=" ")


if __name__ == '__main__':
    main()
