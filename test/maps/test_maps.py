import unittest

from maps.maps import ListMap
from util.map_util import ValueMissingError


class TestMaps(unittest.TestCase):

    def test_basic_list_map_get_put(self):
        list_map = ListMap()
        list_map.put("a", 1)
        actual = list_map.get("a")
        self.assertTrue(actual == 1)

    def test_basic_list_map_put_duplicate(self):
        list_map = ListMap()
        list_map.put("a", 1)
        list_map.put("a", 2)
        actual = list_map.get("a")
        self.assertTrue(actual == 2)

    def test_basic_list_map_get_none(self):
        list_map = ListMap()
        list_map.put("a", 1)
        actual = list_map.get("dne")
        self.assertTrue(actual is None)

    def test_basic_list_map_get_with_collisions(self):
        # Size of 1 means there must be collisions with multiple entries, in this case behaves like a list.
        list_map = ListMap(size=1)
        list_map.put("a", 1)
        list_map.put("b", 2)
        list_map.put("c", 3)

        self.assertTrue(list_map.get("a") == 1)
        self.assertTrue(list_map.get("b") == 2)
        self.assertTrue(list_map.get("c") == 3)

    def test_basic_list_map_remove_exists(self):
        list_map = ListMap(size=1)
        list_map.put("a", 1)
        list_map.remove("a")
        actual = list_map.get("a")
        self.assertTrue(actual is None)

    def test_basic_list_map_remove_dne(self):
        list_map = ListMap(size=1)

        try:
            # Should have raised an exception
            list_map.remove("a")
            self.assertTrue(True == False)
        except ValueMissingError:
            pass

        actual = list_map.get("a")
        self.assertTrue(actual is None)


