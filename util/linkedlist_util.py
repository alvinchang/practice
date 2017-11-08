

class LinkedList:

    def __init__(self, head):
        """
        :param head:
        :type head: LinkedListNode
        """
        self._head = head
        self._size = 1

    def set_next(self, node):
        """
        :param node: the linked list node to be set as the next for this current node.
        :type node: LinkedListNode
        """
        self._head.set_next(node)
        self._size += 1

    def remove_node_with_name(self, name):
        """
        Removes a node with a given name.

        :param name:
        :type name: str

        :return:
        """

        # If the node to be removed is the head pointer, update the head to be its next ptr, update size
        current_ptr = self._head
        if current_ptr.name == name:
            self._head = current_ptr.next_node
            self._size -= 1
            return

        # Otherwise, find the node to be removed and update ptrs accordingly.
        current_ptr = current_ptr.next_node
        while current_ptr is not None:

            # Could not find anything to remove.
            if current_ptr.next_node is None:
                return

            # The next node is the node we want to remove, update size.
            if current_ptr.next_node.name == name:
                current_ptr.next_node = current_ptr.next_node.next_node
                self._size -= 1
                return

            current_ptr = current_ptr.next_node

    def append(self, name):
        """
        Appends a node to the end of this linked list.

        :param name: the name of the node to be appended
        :type name: str
        """

        current_ptr = self._head

        # Reach the end of this linked list.
        while current_ptr.next_node is not None:
            current_ptr = current_ptr.next_node

        current_ptr.set_next(LinkedListNode(name))

    def to_string(self):
        """
        Prints a linked list
        """

        current_ptr = self._head

        while current_ptr is not None:
            # Don't include an arrow for the last node.
            arrow = "" if current_ptr.next_node is None else " ->"
            print current_ptr.name + arrow,
            current_ptr = current_ptr.next_node
        print " (size: {})".format(self._size)

    @property
    def head(self):
        """
        :rtype: LinkedListNode
        """
        return self._head

    @property
    def size(self):
        return self._size if self._head is not None else 0


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
    :rtype: LinkedList
    """
    if not node_list:
        return None

    head_node_name = node_list[0]
    head_ptr = LinkedList(LinkedListNode(head_node_name))
    current_ptr = head_ptr
    for _i in xrange(1, len(node_list)):
        node_name = node_list[_i]
        node = LinkedListNode(node_name)
        current_ptr.set_next(node)
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


