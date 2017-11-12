from util.node_util import Node


class LinkedListNode(Node):

    def __init__(self, name):
        """
        :param name: the name of the node.
        :type name: str
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


class InvalidLinkedListIndexError(ValueError):
    pass
