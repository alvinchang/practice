

def generate_permutations_string1(input_string, char_index=0):
    """
    Generates permutations of a string by performing inversions left to right.

    Ex. "abc" returns ["abc", "bac", "cab", "bca", "cba", "acb"]

    :param input_string:
    :return:
    """
    results = []

    if not input_string:
        return input_string

    if char_index == len(input_string) - 1:
        results.append("".join(input_string))

    for _i in xrange(char_index, len(input_string)):

        input_string_list = list(input_string)
        input_string_list[_i], input_string_list[char_index] = input_string_list[char_index], input_string_list[_i]

        results.extend(generate_permutations_string1(input_string_list, char_index=char_index + 1))
    return results


def generate_permutations_string2(input_string):
    """
    Generates permutations via recursion and backtracking

    """
    results = generate_permutations_string2_helper(input_string, 0, len(input_string)-1)
    return results


def swap_string_index(s, idx1, idx2):
    """
    Swaps a string index by turning it into a list, and then swapping the elements at idx1, idx2. This is done
    because strings are immutable and do not support item assignment.

    :param s:
    :type s: str

    :param idx1:
    :type idx1: int

    :param idx2:
    :type
    :return:
    """
    str_list = list(s)
    str_list[idx1], str_list[idx2] = str_list[idx2], str_list[idx1]
    return "".join(str_list)


def generate_permutations_string2_helper(input_string, lower, upper):
    results = []

    if lower == upper:
        results.append(input_string)

    for _i in xrange(lower, upper+1):
        input_string = swap_string_index(input_string, _i, lower)
        results.extend(generate_permutations_string2_helper(input_string, lower+1, upper))
        # backtrack
        input_string = swap_string_index(input_string, _i, lower)
    return results





