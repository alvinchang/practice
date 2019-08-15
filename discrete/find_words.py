def find_min_words(string, dictionary):
    """
    Finds the minimum number of substrings in a string (no whitespaces) where each substring is in the dictionary.

    :param string:
    :param dictionary:
    :return:
    """
    # If string or dict is empty, no valid words.
    if not string or not dictionary:
        return []
    results = find_min_words_helper(string, set(dictionary), 0, len(string) - 1, [])

    # Find the minimum amount of words
    min_result = min(results, key=lambda x: len(x))
    return min_result


def find_min_words_helper(string, dictionary, lower, end, current_word_list):
    """

    :param string:
    :param dictionary:
    :param lower:
    :param end:
    :param current_word_list:
    :return:
    """
    results = []

    # Reached past the end, return current word list.
    if lower > end:
        return [current_word_list]

    # Iterate over the string from the lower starting point, up until the end.
    for _i in xrange(lower, end + 1):

        # the substring in consideration
        substring = string[lower:_i + 1]

        # If the substring is found in the dictionary, add the substring to the current list of words
        # and set the lower index to be the index after the upper index of the valid word
        if substring in dictionary:
            current_word_list_copy = current_word_list[:]
            current_word_list_copy.append(substring)
            result = find_min_words_helper(string, dictionary,
                                           lower=_i + 1,
                                           end=end,
                                           current_word_list=current_word_list_copy)
            results.extend(result)

    return results


if __name__ == "__main__":
    example_string = "goodweather"
    example_dict_list = ['good', 'weather', 'we', 'at', 'her']
    actual = find_min_words(example_string, example_dict_list)
    # Note in this case we dont want, 'good', 'we', 'at', 'her' since its longer
    expected = ['good', 'weather']
    assert actual == expected

    example_string = "helloworld!"
    example_dict_list = ['he', 'hell', 'low', 'hello', 'world', '!']
    actual = find_min_words(example_string, example_dict_list)
    expected = ['hello', 'world', '!']
    assert actual == expected
