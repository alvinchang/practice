from util.node_util import Node, KVPair


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

    def set_value(self, value):
        if isinstance(self._identifier, KVPair):
            self._identifier.set_value(value)
        else:
            raise NotImplementedError

    @property
    def identifier(self):
        # Custom functionality to pass through the key for a KV Pair to be used in comparisons, initially was expecting
        # only to use single dimensional identifiers like a str or int.
        if isinstance(self._identifier, KVPair):
            return self._identifier.key
        else:
            return self._identifier

    @property
    def value(self):
        # Custom functionality to pass through the value for a KV Pair to be used in comparisons, initially was
        # expecting only to use single dimensional identifiers like a str or int.
        if isinstance(self._identifier, KVPair):
            return self._identifier.value
        else:
            return self._identifier


class InvalidLinkedListIndexError(ValueError):
    pass


class LinkedListValueMissingError(ValueError):
    pass
