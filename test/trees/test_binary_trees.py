import unittest
from random import shuffle

from util.tree_util import BinaryTreeNode
from trees.trees import BinaryTree, BinaryTreeReaderWriter


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

    def test_basic_binary_tree_levelorder_path(self):
        binary_tree = TestBinaryTree.create_basic_binary_tree()
        path = binary_tree.level_order_traversal_path()
        expected_path = ['A', 'B', 'C', 'D', 'E', 'F']
        self.assertEqual(path, expected_path)

    def test_basic_binary_tree_equality(self):
        binary_tree = TestBinaryTree.create_basic_binary_tree()
        binary_tree_same = TestBinaryTree.create_basic_binary_tree()
        self.assertTrue(binary_tree.is_equal(binary_tree_same))
        self.assertTrue(binary_tree_same.is_equal(binary_tree))

    def test_basic_binary_tree_not_equal(self):
        binary_tree = TestBinaryTree.create_basic_binary_tree()
        binary_tree_2 = TestBinaryTree.create_basic_binary_tree_2()
        self.assertFalse(binary_tree.is_equal(binary_tree_2))
        self.assertFalse(binary_tree_2.is_equal(binary_tree))

    def test_basic_binary_tree_height_one_node(self):
        binary_tree = TestBinaryTree.create_basic_binary_tree_one_node()
        self.assertEqual(binary_tree.height(), 1)

    def test_basic_binary_tree_height(self):
        binary_tree = TestBinaryTree.create_basic_binary_tree()
        self.assertEqual(binary_tree.height(), 3)

    def test_basic_binary_tree_creation(self):
        int_list = range(1, 8)
        shuffle(int_list)
        binary_tree = BinaryTree.create_bst(int_list)
        actual_path = binary_tree.in_order_traversal_path()
        expected_path = sorted(int_list)
        self.assertEquals(actual_path, expected_path)

        expected_tree = TestBinaryTree.create_basic_binary_search_tree_ints()
        print expected_tree.in_order_traversal_path()
        self.assertTrue(binary_tree.is_equal(expected_tree))

    @staticmethod
    def create_basic_binary_tree_one_node():
        """
            Sample adj map

                   A

            """

        sample_adj_map = {
            "A": [None, None]
        }
        return TestBinaryTree.generate_binary_tree(sample_adj_map, "A")

    @staticmethod
    def create_basic_binary_search_tree_ints():
        """
            Sample adj map

                   4
                  / \
                 2   6
                / \  /\
               1  3 5  7

            """

        sample_adj_map = {
            2: [1, 3],
            4: [2, 6],
            6: [5, 7],
        }
        return TestBinaryTree.generate_binary_tree(sample_adj_map, 4)

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
    def create_basic_binary_tree_2():
        """
            Sample adj map

                   A
                  / \
                 B   C
                / \  /
               D   E F

            """

        sample_adj_map = {
            "A": ["B", "C"],
            "B": ["D", "E"],
            "C": ["F", None]
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
        :type starting_node_name: str or int

        :return:
        """

        node_name_set = set(starting_node_name) if isinstance(starting_node_name, str) else set([starting_node_name])
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


class TestBinaryTreesReaderWriter(unittest.TestCase):

    def test_basic_binary_tree_de_and_serialization_with_level_order_traversal(self):
        binary_tree = TestBinaryTree.create_basic_binary_tree()
        level_order_path = binary_tree.level_order_traversal_path()
        print level_order_path


    def test_basic_binary_tree_de_and_serialization_1(self):
        binary_tree = TestBinaryTree.create_basic_binary_tree()
        in_order, pre_order = BinaryTreeReaderWriter.serialize_1(binary_tree)
        print "in_order={}".format(in_order)
        print "pre_order={}".format(pre_order)
        new_binary_tree = BinaryTreeReaderWriter.deserialize_1(in_order, pre_order)
        print "in_order={}".format(new_binary_tree.in_order_traversal_path())
        print "pre_order={}".format(new_binary_tree.pre_order_traversal_path())
        #self.assertTrue(binary_tree.is_equal(new_binary_tree))
        #self.assertTrue(new_binary_tree.is_equal(binary_tree))
