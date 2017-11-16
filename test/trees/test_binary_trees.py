import unittest

from util.tree_util import BinaryTreeNode
from trees.trees import BinaryTree


class TestBinaryTree(unittest.TestCase):

    def test_basic_binary_tree_inorder_path(self):
        binary_tree = TestBinaryTree.create_basic_binary_tree()
        path = binary_tree.in_order_traversal_path()
        expected_path = ["D", "B", "E", "A", "C", "F"]
        self.assertTrue(path == expected_path)

    def test_basic_binary_tree_postorder_path(self):
        binary_tree = TestBinaryTree.create_basic_binary_tree()
        path = binary_tree.post_order_traversal_path()
        expected_path = ["D", "B", "E", "C", "F", "A"]
        self.assertTrue(path == expected_path)

    def test_basic_binary_tree_preorder_path(self):
        binary_tree = TestBinaryTree.create_basic_binary_tree()
        path = binary_tree.pre_order_traversal_path()
        expected_path = ["A", "D", "B", "E", "C", "F"]
        self.assertTrue(path == expected_path)

    @staticmethod
    def create_basic_binary_tree():
        """
            Sample adj map

                   A
                  / \
                 B   C
                / \   \
               D   E   F

            """

        sample_adj_map = {
            "A": ["B", "C"],
            "B": ["D", "E"],
            "C": [None, "F"]
        }
        return TestBinaryTree.generate_binary_tree(sample_adj_map, "A")

    @staticmethod
    def generate_binary_tree(adj_map, starting_node_name):
        """
        Ex:
        A: [B, C]
        B: [D, E]
        D: [None, F]

        Creates a binary tree of the following form:

                  A
                 /\
                B C
               /\  \
              D E  F

        :param adj_map: the adjacency map used as a basis to construct the binary tree, in the following form:
                ${parent_node}: [${left_child}, ${right_child}]
        :type adj_map: dict

        :param starting_node_name: the node that the binary tree starts with
        :type starting_node_name: str

        :return:
        """

        node_name_set = set(starting_node_name)
        for (left_child_name, right_child_name) in adj_map.itervalues():
            node_children_set = {left_child_name, right_child_name}
            node_name_set.update(node_children_set)

        node_map = {_node_name: BinaryTreeNode(_node_name) for _node_name in node_name_set if _node_name is not None}

        # Iterate through each parent: left_child, right_child in the adj map and adjust ptrs accordingly.
        for parent_node_name, (left_child_name, right_child_name) in adj_map.iteritems():
            parent_node = node_map[parent_node_name]
            left_node = None if left_child_name is None else node_map[left_child_name]
            right_node = None if right_child_name is None else node_map[right_child_name]
            parent_node.set_left(left_node)
            parent_node.set_right(right_node)

        return BinaryTree(node_map[starting_node_name])
