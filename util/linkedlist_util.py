

class LinkedListNode:

    def __init__(self, name):
        """
        :param name: the name of the node.
        :type name: str
        """
        self._name = name
        self._next_node = None

    def set_next(self, node):
        """
        :param node: the linked list node to be set as the next for this current node.
        :type node: LinkedListNode
        """
        self._next_node = node

    @property
    def next_node(self):
        return self._next_node

    @property
    def name(self):
        return self._name


def generate_linked_list(node_list):
    """
    Generates a basic linked list.

    Ex. ['A', 'B', 'C'] => A -> B -> C
    :param node_list: a list of node names to construct a linked list with in order.
    :return: the header of the linked list.
    :rtype: LinkedListNode
    """
    if not node_list:
        return None

    head_node_name = node_list[0]
    head_ptr = LinkedListNode(head_node_name)
    current_ptr = head_ptr
    for _i in xrange(1, len(node_list)):
        node_name = node_list[_i]
        node = LinkedListNode(node_name)
        current_ptr.set_next(node)
        current_ptr = node

    return head_ptr


def print_linked_list(linked_list_node):
    """
    Prints a linked list

    :param linked_list_node:
    :type linked_list_node: LinkedListNode

    """

    curr_ptr = linked_list_node
    nodes = []
    while curr_ptr is not None:
        nodes.append(curr_ptr.name)
        curr_ptr = curr_ptr.next_node
    print " -> ".join(nodes)


if __name__ == "__main__":
    head = generate_linked_list(["A", "B", "C"])
    print_linked_list(head)


