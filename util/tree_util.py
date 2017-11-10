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
            path.append(node.name)
            BinaryTree.in_order_traversal_pather(node.right, path)

    @staticmethod
    def pre_order_traversal_pather(node, path):
        if node is not None:
            path.append(node.name)
            BinaryTree.in_order_traversal_pather(node.left, path)
            BinaryTree.in_order_traversal_pather(node.right, path)

    @staticmethod
    def post_order_traversal_pather(node, path):
        if node is not None:
            BinaryTree.in_order_traversal_pather(node.left, path)
            BinaryTree.in_order_traversal_pather(node.right, path)
            path.append(node.name)

    @staticmethod
    def in_order_traversal_printer(node, level=0):
        if node is not None:
            BinaryTree.in_order_traversal_printer(node.left, level=level + 1)
            print "\t" * level + node.name
            BinaryTree.in_order_traversal_printer(node.right, level=level + 1)

    @staticmethod
    def pre_order_traversal_printer(node, level=0):
        if node is not None:
            print "\t" * level + node.name
            BinaryTree.pre_order_traversal_printer(node.left, level=level + 1)
            BinaryTree.pre_order_traversal_printer(node.right, level=level + 1)

    @staticmethod
    def post_order_traversal_printer(node, level=0):
        if node is not None:
            BinaryTree.pre_order_traversal_printer(node.left, level=level + 1)
            BinaryTree.pre_order_traversal_printer(node.right, level=level + 1)
            print "\t" * level + node.name


class BinaryTreeNode(Node):

    def __init__(self, name):
        super(BinaryTreeNode, self).__init__(name)
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


if __name__ == "__main__":
    # sample adjacency map
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

    binary_tree = generate_binary_tree(sample_adj_map, starting_node_name="A")
    # binary_tree.print_in_order_traversal()
    print binary_tree.in_order_traversal_path()

















