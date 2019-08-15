import itertools
import unittest

from discrete.combination import generate_combinations


class TestCombinations(unittest.TestCase):

    def test_basic_combinations(self):
        input_list = [1, 2, 3]
        actual_combo_set = set(generate_combinations([1, 2, 3]))

        expected_combo_set = set()
        for _i in xrange(0, len(input_list) + 1):
            length_expected_set = set(itertools.combinations(input_list, _i))
            expected_combo_set.update(length_expected_set)

        self.assertEqual(actual_combo_set, expected_combo_set)

    def test_basic_combinations_2(self):
        input_list = [1, 2, 3, 4, 5, 6, 7, 8]
        actual_combo_set = set(generate_combinations(input_list))

        expected_combo_set = set()
        for _i in xrange(0, len(input_list) + 1):
            length_expected_set = set(itertools.combinations(input_list, _i))
            expected_combo_set.update(length_expected_set)

        self.assertEqual(actual_combo_set, expected_combo_set)

    def test_basic_combinations_empty(self):
        input_list = []
        actual_combo_set = set(generate_combinations(input_list))

        expected_combo_set = set()
        for _i in xrange(0, len(input_list) + 1):
            length_expected_set = set(itertools.combinations(input_list, _i))
            expected_combo_set.update(length_expected_set)

        self.assertEqual(actual_combo_set, expected_combo_set)
