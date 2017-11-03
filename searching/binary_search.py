from random import randint, sample


def binary_search_recursive(arr, value, index=0):
    """
    Performs binary search in a recursive fashion.

    :param arr: a sorted list
    :type arr: list

    :param value:
    :type value: int

    :param index: the index that the value occurs in
    :type index: int

    :return: the value, index if it exists or None if it does not
    :rtype: int or NoneType
    """

    if not arr:
        return None

    midpoint_idx = len(arr) / 2
    midpoint_val = arr[midpoint_idx]

    if midpoint_val == value:
        return index + midpoint_idx
    elif value < midpoint_val:
        return binary_search_recursive(arr[0:midpoint_idx], value, index=index)
    else:
        return binary_search_recursive(arr[midpoint_idx::], value, index=index + midpoint_idx)


def binary_search_iterative(arr, value, index=0):
    """
    Performs binary search in an iterative fashion.

    :param arr: a sorted list
    :type arr: list

    :param value:
    :type value: int

    :param index: the index that the value occurs in
    :type index: int

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


def get_all_indices(arr, value):
    """
    Gets all the indices of a value in an arr if it exists.

    :param arr:
    :type arr: list

    :param value:
    :type value: int

    :return: a list of indices for which the value occurs, empty list if it never occurs.
    :rtype: list
    """
    res = []
    for _i, _val in enumerate(arr):
        if _val == value:
            res.append(_i)
    return res


if __name__ == "__main__":
    total_list_size = 10
    random_list_upper_bound = 100
    random_list = [randint(0, random_list_upper_bound) for _ in xrange(0, total_list_size)]
    random_list.sort()

    # Recursive test

    # Should find something here as we sampled from the actual random list of integers.
    random_value_exists = sample(random_list, 1)[0]
    print "Finding {} in list={}".format(random_value_exists, random_list)
    value_indices = get_all_indices(random_list, random_value_exists)
    print "Valid indices={}".format(value_indices)

    result = binary_search_recursive(random_list, random_value_exists)
    if result in value_indices:
        print "pass"
    else:
        print "fail"
        exit(1)

    # Should not find something here as we sampled from the list of integers that are not present.
    random_list_complement = [_x for _x in xrange(0, random_list_upper_bound) if _x not in random_list]
    random_value_dne = sample(random_list_complement, 1)[0]
    print "Finding {} in list={}".format(random_value_dne, random_list_complement)
    value_indices = get_all_indices(random_list, random_value_dne)
    print "Valid indices={}".format(value_indices)

    result = binary_search_recursive(random_list_complement, random_value_dne)
    if result not in value_indices:
        print "pass"
    else:
        print "fail"
        exit(1)

    # Iterative test

    # Should find something here as we sampled from the actual random list of integers.
    random_value_exists = sample(random_list, 1)[0]
    print "Finding {} in list={}".format(random_value_exists, random_list)
    value_indices = get_all_indices(random_list, random_value_exists)
    print "Valid indices={}".format(value_indices)

    result = binary_search_iterative(random_list, random_value_exists)
    if result in value_indices:
        print "pass"
    else:
        print "fail"
        exit(1)

    # Should not find something here as we sampled from the list of integers that are not present.
    random_list_complement = [_x for _x in xrange(0, random_list_upper_bound) if _x not in random_list]
    random_value_dne = sample(random_list_complement, 1)[0]
    print "Finding {} in list={}".format(random_value_dne, random_list_complement)
    value_indices = get_all_indices(random_list, random_value_dne)
    print "Valid indices={}".format(value_indices)

    result = binary_search_iterative(random_list_complement, random_value_dne)
    if result not in value_indices:
        print "pass"
    else:
        print "fail"
        exit(1)
