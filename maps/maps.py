from util.map_util import Map, ValueMissingError


class ListMap(Map):
    """
    Basic implementation of a map that uses a python list to chain collisions. Note that we could use a linked list,
    binary search tree, or another data structure that best suits the use case for iterating through collisions.
    """

    def __init__(self, size=31):
        super(ListMap, self).__init__(list, size)

    def get(self, key):
        key_hash = self.hash(key)
        for (chained_key, chained_value) in self._chain_map[key_hash]:
            if chained_key == key:
                return chained_value
        return None

    def put(self, key, value):
        key_hash = self.hash(key)
        kv_pair = (key, value)
        # If the value already exists, update it.
        for _idx, (chained_key, chained_value) in enumerate(self._chain_map[key_hash]):
            if chained_key == key:
                self._chain_map[key_hash][_idx] = kv_pair
        # Otherwise add it to the end of the list.
        self._chain_map[key_hash].append(kv_pair)

    def _remove_key(self, key):
        key_hash = self.hash(key)
        for _idx, (chained_key, chained_value) in enumerate(self._chain_map[key_hash]):
            if chained_key == key:
                self._chain_map[key_hash].pop(_idx)
        return None

    def remove(self, key):
        key_hash = self.hash(key)
        for _idx, (chained_key, chained_value) in enumerate(self._chain_map[key_hash]):
            if chained_key == key:
                self._chain_map[key_hash].pop(_idx)
                return
        raise ValueMissingError()



