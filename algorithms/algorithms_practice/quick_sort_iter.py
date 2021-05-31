"""Python program for implementation of iterative Quicksort"""


def splitter(array, low, high):
    """A function that splits an array

    Parameters

    low - starting boundary value
    high - starting boundary value
    array - entered list

    """
    i = (low - 1)
    x = array[high]
    for j in range(low, high):
        if array[j] <= x:
            i = i + 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1


def quickSortIter(arr, low, high):
    """Main function of sorting"""
    size_list = high - low + 1
    stack = [0] * size_list
    top = -1
    top = top + 1
    stack[top] = low
    top = top + 1
    stack[top] = high

    while top >= 0:

        high = stack[top]
        top = top - 1
        low = stack[top]
        top = top - 1
        split = splitter(arr, low, high)

        if split - 1 > low:
            top = top + 1
            stack[top] = low
            top = top + 1
            stack[top] = split - 1

        if split + 1 < high:
            top = top + 1
            stack[top] = split + 1
            top = top + 1
            stack[top] = high


def main():
    array = [14, 32, 15, 12, 11, 32, 23, 36]
    n = len(array)
    quickSortIter(array, 0, n - 1)
    print("Sorted array:")
    for elem in array:
        print(elem, end=' ')


if __name__ == '__main__':
    main()
