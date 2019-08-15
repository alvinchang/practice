import unittest

from maps.maps import ListMap, LinkedListMap
from util.map_util import ValueMissingError


class TestMaps(unittest.TestCase):

    def test_all_maps(self):

        for map_type in (LinkedListMap, ListMap):
            self.basic_map_get_put(map_type)
            self.basic_map_put_duplicate(map_type)
            self.basic_map_get_none(map_type)
            self.basic_list_map_get_with_collisions(map_type)
            self.basic_list_map_remove_exists(map_type)
            self.basic_list_map_remove_dne(map_type)

    def basic_map_get_put(self, map_type):
        test_map = map_type()
        test_map.put("a", 1)
        actual = test_map.get("a")
        self.assertTrue(actual == 1)

    def basic_map_put_duplicate(self, map_type):
        test_map = map_type()
        test_map.put("a", 1)
        test_map.put("a", 2)
        actual = test_map.get("a")
        self.assertTrue(actual == 2)

    def basic_map_get_none(self, map_type):
        test_map = map_type()
        test_map.put("a", 1)
        actual = test_map.get("dne")
        self.assertTrue(actual is None)

    def basic_list_map_get_with_collisions(self, map_type):
        # Size of 1 means there must be collisions with multiple entries, in this case behaves like a list.
        test_map = map_type(size=1)
        test_map.put("a", 1)
        test_map.put("b", 2)
        test_map.put("c", 3)

        self.assertTrue(test_map.get("a") == 1)
        self.assertTrue(test_map.get("b") == 2)
        self.assertTrue(test_map.get("c") == 3)

    def basic_list_map_remove_exists(self, map_type):
        test_map = map_type(size=1)
        test_map.put("a", 1)
        test_map.remove("a")
        actual = test_map.get("a")
        self.assertTrue(actual is None)

    def basic_list_map_remove_dne(self, map_type):
        test_map = map_type(size=1)

        try:
            # Should have raised an exception
            test_map.remove("a")
            self.assertTrue(False)
        except ValueMissingError:
            pass

        actual = test_map.get("a")
        self.assertTrue(actual is None)
