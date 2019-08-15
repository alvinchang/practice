import unittest
from random import randint

from sorting.bubble_sort import bubble_sort
from sorting.merge_sort import merge_sort
from sorting.quick_sort import quick_sort, PivotSelectionType


class TestSorting(unittest.TestCase):

    def test_basic_merge_sort(self):
        random_list = [randint(0, 1000) for _ in xrange(0, 1000)]
        expected = sorted(random_list)
        actual = merge_sort(random_list)
        self.assertTrue(expected == actual)

    def test_bubble_sort(self):
        random_list = [randint(0, 1000) for _ in xrange(0, 1000)]
        expected = sorted(random_list)
        actual = bubble_sort(random_list)
        self.assertTrue(expected == actual)

    def test_basic_quick_sort_first_pivot(self):
        random_list = [randint(0, 1000) for _ in xrange(0, 1000)]
        expected = sorted(random_list)
        actual = quick_sort(random_list, PivotSelectionType.FIRST)
        self.assertTrue(expected == actual)

    def test_basic_quick_sort_last_pivot(self):
        random_list = [randint(0, 1000) for _ in xrange(0, 1000)]
        expected = sorted(random_list)
        actual = quick_sort(random_list, PivotSelectionType.LAST)
        self.assertTrue(expected == actual)

    def test_basic_quick_sort_median_pivot(self):
        random_list = [randint(0, 1000) for _ in xrange(0, 1000)]
        expected = sorted(random_list)
        actual = quick_sort(random_list, PivotSelectionType.MEDIAN)
        self.assertTrue(expected == actual)
