from util.node_util import Node


class BinaryTreeNode(Node):

    NONE_ID = "#"

    def __init__(self, identifier):
        super(BinaryTreeNode, self).__init__(identifier)
        self._left = None
        self._right = None

    def set_left(self, node):
        """
        :param node:
        :type node: BinaryTreeNode
        """
        self._left = node

    def set_right(self, node):
        """
       :param node:
       :type node: BinaryTreeNode
       """
        self._right = node

    @property
    def left(self):
        """
        :rtype: BinaryTreeNode
        """
        return self._left

    @property
    def right(self):
        """
        :rtype: BinaryTreeNode
        """
        return self._right


class NaryTreeNode(Node):

    def __init__(self, identifier):
        super(NaryTreeNode, self).__init__(identifier)
        self._children = []

    @property
    def children(self):
        return self._children












