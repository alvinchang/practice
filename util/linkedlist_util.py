from util.map_util import KVPair
from util.node_util import Node


class LinkedListNode(Node):

    def __init__(self, identifier):
        """
        :param identifier: the name of the node.
        :type identifier: str or KVPair
        """
        super(LinkedListNode, self).__init__(identifier)
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
        if isinstance(self._identifier, KVPair):
            return self._identifier.key
        else:
            return super(LinkedListNode, self).identifier


class InvalidLinkedListIndexError(ValueError):
    pass


class LinkedListValueMissingError(ValueError):
    pass
