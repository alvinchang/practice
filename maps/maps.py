from linkedlists.linkedlists import SinglyLinkedList
from util.linkedlist_util import LinkedListValueMissingError
from util.map_util import Map, ValueMissingError, KVPair


class ListMap(Map):
    """
    Basic implementation of a map that uses a python list to chain collisions. Note that we could use a linked list,
    binary search tree, or another data structure that best suits the use case for iterating through collisions.
    """

    def __init__(self, size=31):
        super(ListMap, self).__init__(list, size)

    def get(self, key):
        key_hash = self.hash(key)
        for _kv_pair in self._chain_map[key_hash]:
            if _kv_pair.key == key:
                return _kv_pair.value
        return None

    def put(self, key, value):
        key_hash = self.hash(key)
        kv_pair = KVPair(key, value)
        # If the value already exists, update it.
        for _idx, _kv_pair in enumerate(self._chain_map[key_hash]):
            if _kv_pair.key == key:
                self._chain_map[key_hash][_idx] = kv_pair
        # Otherwise add it to the end of the list.
        self._chain_map[key_hash].append(kv_pair)

    def _remove_key(self, key):
        key_hash = self.hash(key)
        for _idx, _kv_pair in enumerate(self._chain_map[key_hash]):
            if _kv_pair.key == key:
                self._chain_map[key_hash].pop(_idx)
        return None

    def remove(self, key):
        key_hash = self.hash(key)
        for _idx, _kv_pair in enumerate(self._chain_map[key_hash]):
            if _kv_pair.key == key:
                self._chain_map[key_hash].pop(_idx)
                return
        raise ValueMissingError()


class LinkedListMap(Map):
    """
    Implementation of a Map backed by a linked list.
    """

    def __init__(self, size=31):
        super(LinkedListMap, self).__init__(SinglyLinkedList, size)

    def get(self, key):

        key_hash = self.hash(key)
        linked_list = self.chain_map[key_hash]

        # Iterate through the linked list, and return the value if you can find it, otherwise return None.
        curr_ptr = linked_list.head
        while curr_ptr is not None:

            if curr_ptr.identifier == key:
                return curr_ptr.identifier.value

            curr_ptr = curr_ptr.next_node

        return None

    def put(self, key, value):
        key_hash = self.hash(key)
        linked_list = self.chain_map[key_hash]

        # Iterate through the linked list, and update the value if you can find it, otherwise insert it.
        curr_ptr = linked_list.head
        while curr_ptr is not None:

            if curr_ptr.identifier.key == key:
                # Update value if key is present.
                curr_ptr.identifier.set_value(value)
                return

            curr_ptr = curr_ptr.next_node
        kv_pair = KVPair(key, value)
        linked_list.append(kv_pair)

    def remove(self, key):
        key_hash = self.hash(key)
        linked_list = self.chain_map[key_hash]
        try:
            linked_list.remove_node_with_name(key)
        except LinkedListValueMissingError:
            raise ValueMissingError()



