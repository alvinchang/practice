from random import randint


def merge_sort(arr):
    """
    :param arr: the array to sort
    :type arr: list
    :return: the sorted array
    :rtype: list
    """

    if len(arr) <= 1:
        return arr

    # Recursively partition left, right halves, then combine sorted lists of length 2
    midpoint_idx = len(arr) / 2
    left = arr[0:midpoint_idx]
    right = arr[midpoint_idx::]

    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)
    result = combine(sorted_left, sorted_right)
    return result


def combine(left, right):
    """
    :type left: list
    :type right: list
    :return: the sorted list
    :rtype: list
    """

    if len(left) == 0:
        return right
    if len(right) == 0:
        return left

    result = []

    while len(left) > 0 and len(right) > 0:

        # If there are no more elements of one partition, break early and append the non empty one to the result.
        if len(left) == 0 or len(right) == 0:
            break

        left_first_element = left[0]
        right_first_element = right[0]

        if left_first_element < right_first_element:
            # If the left is smaller, add left first element to result and remove from the left array
            result.append(left_first_element)
            left.pop(0)
        else:
            # If the right is smaller, add right first element to result and remove from the right array
            result.append(right_first_element)
            right.pop(0)

    # Add the remaining parts of the array if non empty
    if len(left) > 0:
        result.extend(left)
    if len(right) > 0:
        result.extend(right)

    return result


if __name__ == "__main__":
    random_list = [randint(0, 1000) for _ in xrange(0, 1000)]
    sorted_list = merge_sort(random_list)
    random_list.sort()
    if random_list == sorted_list:
        print 'pass'
    else:
        print 'fail'


