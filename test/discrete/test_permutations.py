import unittest
from itertools import permutations

from discrete.permutation import generate_permutations_string1, generate_permutations_string2


class TestPermutations(unittest.TestCase):

    def test_all_permutations(self):
        for permute_string_method in (generate_permutations_string1, generate_permutations_string2):
            self.permutations_basic(permute_string_method)
            self.permutations_empty(permute_string_method)

    def permutations_basic(self, permute_string_method):
        basic_string = "abcdef"
        actual_perms = set(permute_string_method(basic_string))
        expected_perms = set("".join(_p) for _p in permutations(basic_string))
        self.assertTrue(actual_perms == expected_perms)

    def permutations_empty(self, permute_string_method):
        empty_string = " "
        actual_perms = set(permute_string_method(empty_string))
        expected_perms = set("".join(_p) for _p in permutations(empty_string))
        self.assertTrue(actual_perms == expected_perms)
