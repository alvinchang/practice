import unittest
from itertools import permutations

from discrete.permutation import generate_permutations


class TestPermutations(unittest.TestCase):

    def test_permutations_basic(self):
        basic_string = "abcdef"
        actual_perms = set(generate_permutations(basic_string))
        expected_perms = set("".join(_p) for _p in permutations(basic_string))
        self.assertTrue(actual_perms == expected_perms)

    def test_permutations_empty(self):
        empty_string = " "
        actual_perms = set(generate_permutations(empty_string))
        expected_perms = set("".join(_p) for _p in permutations(empty_string))
        self.assertTrue(actual_perms == expected_perms)

