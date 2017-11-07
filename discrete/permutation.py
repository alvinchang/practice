

def generate_permutations(input_string, char_index=0):
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

        results.extend(generate_permutations(input_string_list, char_index=char_index+1))
    return results




