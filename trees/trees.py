from graphs.traversals import process_node
from util.tree_util import BinaryTreeNode


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

    @property
    def head(self):
        """
        :rtype: BinaryTreeNode
        """
        return self._head

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

    def is_equal(self, other_tree):
        """
        :param other_tree:
        :type other_tree: BinaryTree
        :return:
        """
        return is_equal(self.head, other_tree.head)


def is_equal(binary_tree_node1, binary_tree_node2):
    """
    Checks whether or not both binary trees denoted by their starting node have equal values for each node and the
    same structure.

    :param binary_tree_node1:
    :type binary_tree_node1: BinaryTreeNode

    :param binary_tree_node2:
    :type: binary_tree1_node: BinaryTreeNode
    """

    # If both nodes are empty, the subtree is equal.
    if binary_tree_node1 is None and binary_tree_node2 is None:
        return True
    # If both nodes are not empty, check the value at the node, and recursively check left and right subtrees
    elif binary_tree_node1 is not None and binary_tree_node2 is not None:
        return binary_tree_node1.identifier == binary_tree_node2.identifier and \
               is_equal(binary_tree_node1.left, binary_tree_node2.left) and \
               is_equal(binary_tree_node1.right, binary_tree_node2.right)
    # In order to reach this case, one of them is not None while the other is, which means this subtree is not equal
    else:
        return False


class BinaryTreeReaderWriter:

    pass







class SuffixTree:

    def __init__(self):
        pass

