from random import randint


def bubble_sort(arr):
    """
    :param arr: the array to sort
    :type arr: list

    :return: the sorted array
    :rtype: list
    """

    # Perform pair swaps until the array is sorted.

    while not check_sorted(arr):
        for _i in xrange(1, len(arr)):
            curr = arr[_i]
            prev = arr[_i - 1]

            # If the previous element is greater than the current element, swap them.
            if prev > curr:
                arr[_i - 1], arr[_i] = arr[_i], arr[_i - 1]
    return arr


def check_sorted(arr):
    """
    Checks if an array is sorted
    :param arr:
    :type arr: list

    :rtype: bool
    """

    for _i in xrange(1, len(arr)):
        curr = arr[_i]
        prev = arr[_i - 1]

        if curr < prev:
            return False

    return True


if __name__ == "__main__":
    random_list = [randint(0, 1000) for _ in xrange(0, 1000)]
    sorted_list = bubble_sort(random_list)
    random_list.sort()
    if random_list == sorted_list:
        print 'pass'
    else:
        print 'fail'
