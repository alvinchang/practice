from util.node_util import Node


class BinaryTree:

    def __init__(self, starting_node):
        """

        :param starting_node:
        :type starting_node: BinaryTreeNode
        """
        self._head = starting_node

    def print_in_order_traversal(self):
        BinaryTree.in_order_traversal_printer(self._head)

    def print_post_order_traversal(self):
        BinaryTree.post_order_traversal_printer(self._head)

    def print_pre_order_traversal(self):
        BinaryTree.pre_order_traversal_printer(self._head)

    def in_order_traversal_path(self):
        path = []
        BinaryTree.in_order_traversal_pather(self._head, path)
        return path

    def pre_order_traversal_path(self):
        path = []
        BinaryTree.pre_order_traversal_pather(self._head, path)
        return path

    def post_order_traversal_path(self):
        path = []
        BinaryTree.post_order_traversal_pather(self._head, path)
        return path

    @staticmethod
    def in_order_traversal_pather(node, path):
        if node is not None:
            BinaryTree.in_order_traversal_pather(node.left, path)
            path.append(node.identifier)
            BinaryTree.in_order_traversal_pather(node.right, path)

    @staticmethod
    def pre_order_traversal_pather(node, path):
        if node is not None:
            path.append(node.identifier)
            BinaryTree.in_order_traversal_pather(node.left, path)
            BinaryTree.in_order_traversal_pather(node.right, path)

    @staticmethod
    def post_order_traversal_pather(node, path):
        if node is not None:
            BinaryTree.in_order_traversal_pather(node.left, path)
            BinaryTree.in_order_traversal_pather(node.right, path)
            path.append(node.identifier)

    @staticmethod
    def in_order_traversal_printer(node, level=0):
        if node is not None:
            BinaryTree.in_order_traversal_printer(node.left, level=level + 1)
            print "\t" * level + node.identifier
            BinaryTree.in_order_traversal_printer(node.right, level=level + 1)

    @staticmethod
    def pre_order_traversal_printer(node, level=0):
        if node is not None:
            print "\t" * level + node.identifier
            BinaryTree.pre_order_traversal_printer(node.left, level=level + 1)
            BinaryTree.pre_order_traversal_printer(node.right, level=level + 1)

    @staticmethod
    def post_order_traversal_printer(node, level=0):
        if node is not None:
            BinaryTree.pre_order_traversal_printer(node.left, level=level + 1)
            BinaryTree.pre_order_traversal_printer(node.right, level=level + 1)
            print "\t" * level + node.identifier


class BinaryTreeNode(Node):

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


class SuffixTree:

    def __init__(self):
        pass


class NaryTreeNode(Node):

    def __init__(self, identifier):
        super(NaryTreeNode, self).__init__(identifier)
        self._children = []

    @property
    def children(self):
        return self._children












