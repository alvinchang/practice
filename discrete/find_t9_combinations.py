"""
Find number of telephone combinations with a string of digits with the below map.

"""

num_to_char_map = {
    1: '',
    2: 'abc',
    3: 'def',
    4: 'ghi',
    5: 'jkl',
    6: 'mno',
    7: 'pqrs',
    8: 'tuv',
    9: 'wxyz'
}


def find_combinations(digits_str, index=0, prefix_str=""):
    all_combinations = []

    if index >= len(digits_str):
        # Reached the end of the string during recursion
        return [prefix_str]

    current_digit = int(digits_str[index])
    char_possibilities = num_to_char_map[current_digit]

    if char_possibilities:
        for char in char_possibilities:
            combinations = find_combinations(digits_str, index + 1, prefix_str + char)
            all_combinations.extend(combinations)
    else:
        # in the case where 1 is anywhere - doesnt map to any valid char for T9 mappings.
        combinations = find_combinations(digits_str, index + 1, prefix_str)
        all_combinations.extend(combinations)

    return all_combinations


if __name__ == "__main__":
    print find_combinations('1232')
