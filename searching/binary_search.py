def binary_search_recursive(arr, value):
    """
    Performs binary search in a recursive fashion. Returns None if it did not find anything.

    :param arr: a sorted list
    :type arr: list

    :param value: the value to find
    :type value: int

    :return: the value, index if it exists or None if it does not
    :rtype: int or NoneType
    """
    if not arr:
        return None

    return binary_search_recursive_helper(arr, value, low=0, high=len(arr) - 1)


def binary_search_recursive_helper(arr, value, low, high):
    """
    Performs binary search on the sub array

    :param arr: a sorted sub list
    :type arr: list

    :param value: the value to find
    :type value: int

    :param low: lower boundary index, initially 0
    :type low: int

    :param high: higher boundary index, initially the index of the last element.
    :type high: int

    :return: the value, index if it exists or None if it does not
    :rtype: int or NoneType
    """

    midpoint_idx = (low + high) / 2
    midpoint_val = arr[midpoint_idx]

    if midpoint_val == value:
        return midpoint_idx
    elif low >= high:
        return None
    elif value < midpoint_val:
        # Value is less than the midpoint so look at the left partition
        return binary_search_recursive_helper(arr, value, low=low, high=midpoint_idx - 1)
    else:
        # Value is greater than the midpoint so look at the right partition.
        return binary_search_recursive_helper(arr, value, low=midpoint_idx + 1, high=high)


def binary_search_iterative(arr, value):
    """
    Performs binary search in an iterative fashion.

    :param arr: a sorted list
    :type arr: list

    :param value:
    :type value: int

    :return: the value, index if it exists or None if it does not
    :rtype: int or NoneType
    """

    if not arr:
        return None

    lower_idx = 0
    upper_idx = len(arr) - 1

    while lower_idx <= upper_idx:

        midpoint_idx = (lower_idx + upper_idx) / 2
        midpoint_val = arr[midpoint_idx]

        if midpoint_val == value:
            return midpoint_idx
        elif midpoint_val < value:
            # go to the right side
            lower_idx = midpoint_idx + 1
        else:
            # go to the left side
            upper_idx = midpoint_idx - 1

    return None
