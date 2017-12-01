import Queue
from collections import deque

from graphs.traversals import process_node
from queues.queues import LinkedListQueue
from util.tree_util import BinaryTreeNode


class BinaryTree:

    def __init__(self, starting_node):
        """

        :param starting_node:
        :type starting_node: BinaryTreeNode
        """
        self._head = starting_node

    @classmethod
    def create_bst(cls, id_list):
        """
        Creates a binary search tree with minimal height given a list of identifiers.

        Note these identifiers must be comparable.

        :param id_list:
        :return:
        """
        id_list.sort()
        return BinaryTree(cls._create_bst(id_list, 0, len(id_list)-1))

    @classmethod
    def _create_bst(cls, id_list, lower, upper):

        if lower > upper:
            return None

        midpoint_idx = (lower + upper) / 2
        midpoint_val = id_list[midpoint_idx]

        node = BinaryTreeNode(midpoint_val)
        left = cls._create_bst(id_list, lower=lower, upper=midpoint_idx-1)
        right = cls._create_bst(id_list, lower=midpoint_idx+1, upper=upper)
        node.set_left(left)
        node.set_right(right)

        return node

    def print_in_order_traversal(self):
        BinaryTree.in_order_traversal_printer(self._head)

    def print_post_order_traversal(self):
        BinaryTree.post_order_traversal_printer(self._head)

    def print_pre_order_traversal(self):
        BinaryTree.pre_order_traversal_printer(self._head)

    def level_order_traversal_path(self, append_nones=False):
        path = []
        queue = LinkedListQueue()
        queue.enqueue(self.head)
        while queue.size() > 0:
            node = queue.dequeue()
            path.append(node.identifier)
            if node.left is not None or append_nones:
                queue.enqueue(node.left)
            if node.right is not None or append_nones:
                queue.enqueue(node.right)
        return path

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
    def pre_order_traversal_pather(node, path, append_nones=False):
        if node is not None:
            path.append(node.identifier)
            BinaryTree.in_order_traversal_pather(node.left, path)
            BinaryTree.in_order_traversal_pather(node.right, path)

        # For appending a null terminator
        if append_nones and node is None:
            path.append(node)

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

    def height(self):
        return height(self.head)


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


def height(binary_tree_node):
    """
    Determines the height of a binary tree (max number of levels of nodes)

    :param binary_tree_node:
    :type: binary_tree_node: BinaryTreeNode
    """
    if binary_tree_node is None:
        return 0
    else:
        return max(height(binary_tree_node.left), height(binary_tree_node.right)) + 1


class BinaryTreeReaderWriter:

    @staticmethod
    def serialize_1(binary_tree):
        """
        Serializes a binary tree using its in order and pre order path traversals.

        :param binary_tree:
        :type binary_tree: BinaryTree
        :return:
        """
        in_order_path = BinaryTree.in_order_traversal_path(binary_tree)
        pre_order_path = BinaryTree.pre_order_traversal_path(binary_tree)
        return in_order_path, pre_order_path

    @staticmethod
    def deserialize_1(in_order_path, pre_order_path):
        """
        :param in_order_path:
        :param pre_order_path:
        :return:
        """
        return BinaryTree(BinaryTreeReaderWriter.deserialize_1_helper(in_order_path, pre_order_path))

    @staticmethod
    def deserialize_1_helper(in_order_path, pre_order_path):
        """
        :param in_order_path:
        :param pre_order_path:
        :return:
        """
        # Base Case
        if not in_order_path or not pre_order_path:
            return None

        root_name = pre_order_path[0]
        root = BinaryTreeNode(root_name)
        idx = in_order_path.index(root_name)
        # Remove the root from further calls, as root should be returned in the current call.
        pre_order_path.pop(0)
        root.set_left(BinaryTreeReaderWriter.deserialize_1_helper(pre_order_path=pre_order_path,
                                                                  in_order_path=in_order_path[0:idx]))
        root.set_right(BinaryTreeReaderWriter.deserialize_1_helper(pre_order_path=pre_order_path,
                                                                   in_order_path=in_order_path[idx + 1::]))
        return root

    @staticmethod
    def serialize_level_order(binary_tree):
        """
        :param binary_tree:
        :type binary_tree: BinaryTree
        """

        level_order_path = binary_tree.level_order_traversal_path(append_nones=True)
        print level_order_path


class SuffixTree:

    def __init__(self):
        pass

