from util.map_util import KVPair
from util.node_util import Node


class LinkedListNode(Node):

    def __init__(self, name):
        """
        :param name: the name of the node.
        :type name: str or KVPair
        """
        super(LinkedListNode, self).__init__(name)
        self._next_node = None

    def set_next_node(self, node):
        """
        :param node: the linked list node to be set as the next for this current node.
        :type node: LinkedListNode
        """
        self._next_node = node

    @property
    def next_node(self):
        return self._next_node

    @property
    def identifier(self):
        # Custom functionality to pass through the key for a KV Pair to be used in comparisons, initially was expecting
        # only to use single dimensional identifiers like a str or int.
        if isinstance(self._name, KVPair):
            return self._name.key
        else:
            return super(LinkedListNode, self).name


class InvalidLinkedListIndexError(ValueError):
    pass


class LinkedListValueMissingError(ValueError):
    pass
