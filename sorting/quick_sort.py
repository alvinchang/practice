from random import randint

import numpy
from enum import Enum


def quick_sort(arr, pivot_selection_type):
    """
    :param arr: the sub array to sort
    :type arr: list

    :param pivot_selection_type: the pivot selection type {first, last, median}
    :type pivot_selection_type: int

    :return: the sorted sub array
    :rtype: list
    """

    # Base case where the sub array is empty
    if not arr:
        return arr

    pivot_element = choose_pivot_element(arr, pivot_selection_type)

    middle_partition = [_x for _x in arr if _x == pivot_element]
    lower_partition = [_x for _x in arr if _x < pivot_element]
    upper_partition = [_x for _x in arr if _x > pivot_element]

    return quick_sort(lower_partition, pivot_selection_type) + middle_partition + \
           quick_sort(upper_partition, pivot_selection_type)


class PivotSelectionType(Enum):
    FIRST = 0
    LAST = 1
    MEDIAN = 2


def choose_pivot_element(arr, pivot_selection_type):
    """

    :param arr: the array to choose a pivot element from
    :type arr: list

    :param pivot_selection_type: the pivot selection type enum
    :type pivot_selection_type: int
    :return:
    """

    if pivot_selection_type == PivotSelectionType.FIRST:
        pivot_element = choose_first_pivot(arr)
    elif pivot_selection_type == PivotSelectionType.LAST:
        pivot_element = choose_last_pivot(arr)
    elif pivot_selection_type == PivotSelectionType.MEDIAN:
        pivot_element = choose_median_pivot(arr)
    else:
        raise ValueError("Unrecognized pivot selection type %".format(pivot_selection_type))
    return pivot_element


def choose_first_pivot(arr):
    return arr[0]


def choose_last_pivot(arr):
    return arr[-1]


def choose_median_pivot(arr):
    return numpy.median(arr)


if __name__ == "__main__":
    random_list = [randint(0, 1000) for _ in xrange(0, 1000)]
    sorted_list = quick_sort(random_list, PivotSelectionType.MEDIAN)
    random_list.sort()
    if random_list == sorted_list:
        print 'pass'
    else:
        print 'fail'
