import unittest
from random import randint, sample

from searching.binary_search import binary_search_recursive, binary_search_iterative


class TestSearching(unittest.TestCase):

    def test_basic_binary_search_recursive(self):
        total_list_size = 100
        random_list_upper_bound = 1000
        random_list = [randint(0, random_list_upper_bound) for _ in xrange(0, total_list_size)]
        random_list.sort()

        # Should find something here as we sampled from the actual random list of integers.
        random_value_exists = sample(random_list, 1)[0]
        value_indices = TestSearching.get_all_valid_indices(random_list, random_value_exists)
        result = binary_search_recursive(random_list, random_value_exists)
        print "Finding {} in list={}".format(random_value_exists, random_list)
        print "Valid indices={}, found={}".format(value_indices, result)
        self.assertTrue(result in value_indices)

    def test_basic_binary_search_recursive_dne(self):
        total_list_size = 100
        random_list_upper_bound = 1000
        random_list = [randint(0, random_list_upper_bound) for _ in xrange(0, total_list_size)]
        random_list.sort()

        # Should not find something here as we sampled from the list of integers that are not present.
        random_list_complement = [_x for _x in xrange(0, random_list_upper_bound) if _x not in random_list]
        random_value_dne = sample(random_list_complement, 1)[0]

        result = binary_search_recursive(random_list, random_value_dne)
        self.assertTrue(result is None)

    def test_basic_binary_search_iterative(self):
        total_list_size = 100
        random_list_upper_bound = 1000
        random_list = [randint(0, random_list_upper_bound) for _ in xrange(0, total_list_size)]
        random_list.sort()

        # Should find something here as we sampled from the actual random list of integers.
        random_value_exists = sample(random_list, 1)[0]
        value_indices = TestSearching.get_all_valid_indices(random_list, random_value_exists)
        result = binary_search_iterative(random_list, random_value_exists)
        print "Finding {} in list={}".format(random_value_exists, random_list)
        print "Valid indices={}, found={}".format(value_indices, result)
        self.assertTrue(result in value_indices)

    def test_basic_binary_search_iterative_dne(self):
        total_list_size = 100
        random_list_upper_bound = 1000
        random_list = [randint(0, random_list_upper_bound) for _ in xrange(0, total_list_size)]
        random_list.sort()

        # Should not find something here as we sampled from the list of integers that are not present.
        random_list_complement = [_x for _x in xrange(0, random_list_upper_bound) if _x not in random_list]
        random_value_dne = sample(random_list_complement, 1)[0]

        result = binary_search_iterative(random_list, random_value_dne)
        self.assertTrue(result is None)

    @staticmethod
    def get_all_valid_indices(arr, value):
        """
        Gets all the indices of a value in an arr if it exists. This is done because binary search returns an index
        of a value that exists or not, but there can be duplicate values so hence we check that it returns one of these
        valid indices.

        :param arr:
        :type arr: list

        :param value:
        :type value: int

        :return: a list of indices for which the value occurs, empty list if it never occurs.
        :rtype: list
        """
        res = []
        for _i, _val in enumerate(arr):
            if _val == value:
                res.append(_i)
        return res

