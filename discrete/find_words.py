# Enter your code here. Read input from STDIN. Print output to STDOUT


example_string = "helloworld!"
example_dict_list = ['he', 'hell', 'low', 'hello', 'world', '!']


# - Hello , World, ! # 3 words

# Don't want , hel lo world !

# goodweather

def find_min_words(string, dictionary):
    # if string or dict is empty, no valid words.
    if not string or not dictionary:
        return []
    results = find_min_words_helper(string, dictionary, 0, len(string) - 1)
    min_result = min(results, key=lambda x: len(x))
    return min_result


def find_min_words_helper(string, dictionary, lower, end, current_word_list=[]):
    results = []

    if lower > end:
        return [current_word_list]

    for _i in xrange(lower, end + 1):
        substring = string[lower:_i + 1]
        if substring in dictionary:
            # print "found word={}, lower={}, upper={}".format(substring, lower, _i)
            # Found a word, lets save it for later.
            current_word_list_copy = current_word_list[:]
            current_word_list_copy.append(substring)
            result = find_min_words_helper(string, dictionary, lower=_i + 1, end=end,
                                           current_word_list=current_word_list_copy)
            results.extend(result)

    return results


# example_string = "goodweather"
# example_dict_list = ['good', 'weather', 'we', 'at', 'her']

# print 'hey'
print find_min_words(example_string, example_dict_list)












