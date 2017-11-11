from linkedlists.linkedlists import LinkedList
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


def generate_linked_list(node_list):
    """
    Generates a basic linked list.

    Ex. ['A', 'B', 'C'] => A -> B -> C
    :param node_list: a list of node names to construct a linked list with in order.
    :return: the header of the linked list.
    :rtype: linkedlists.linkedlists.LinkedList
    """
    if not node_list:
        return None

    head_node_name = node_list[0]
    head_ptr = LinkedList(LinkedListNode(head_node_name))
    current_ptr = head_ptr
    for _i in xrange(1, len(node_list)):
        node_name = node_list[_i]
        node = LinkedListNode(node_name)
        current_ptr.set_next_node(node)
        current_ptr = node

    return head_ptr


if __name__ == "__main__":
    # linked_list = LinkedList(generate_linked_list(["A", "B", "C"]))
    # linked_list.to_string()
    # linked_list.append("D")
    # linked_list.to_string()
    #
    # linked_list.remove_node_with_name("D")
    # linked_list.to_string()
    #
    # linked_list.remove_node_with_name("A")
    # linked_list.to_string()

    linked_list = generate_linked_list(["A", "A"])
    linked_list.to_string()
    linked_list.remove_node_with_name("A")
    linked_list.to_string()


