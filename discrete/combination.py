

def generate_combinations(input_list):
    """
    Generates combinations given an input list.

    :param input_list:
    :type input_list: list

    :rtype: List[Tuple]
    """

    result = []
    for idx in xrange(0, 2 ** len(input_list)):
        result.append(get_combination_from_num(input_list, idx))
    return result


def get_combination_from_num(input_list, num):
    """
    Gets the combination given a number.

    i.e. num=6 => 1010  (include item at index 1 and 3)

    :param input_list:
    :type input_list: list

    :param num:
    :type num: int

    :return:
    """
    item_idx = 0
    result = []
    while num > 0:

        bit = num & 1
        if bit:
            result.append(input_list[item_idx])

        item_idx += 1
        num = num >> 1
    return tuple(result)

