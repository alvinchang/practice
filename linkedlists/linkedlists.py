from util.linkedlist_util import LinkedListNode, InvalidLinkedListIndexError


class LinkedList:

    def __init__(self, head):
        """
        :param head:
        :type head: LinkedListNode
        """
        self._head = head
        self._size = 1

    def set_next_node(self, node):
        """
        :param node: the linked list node to be set as the next for this current node.
        :type node: LinkedListNode
        """
        self._head.set_next_node(node)
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
            if current_ptr.name == name:
                current_ptr.set_next_node(current_ptr.next_node.next_node)
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

        current_ptr.set_next_node(LinkedListNode(name))

    def insert_at_position(self, name, index):
        """
        Inserts a node at the given position of this linked list.

        :param name: the name of the node to be inserted.
        :type name: str

        :param index: the position of the node to be inserted.
        :type index: int

        :raise: InvalidLinkedListIndexError
        """

        current_ptr = self._head

        new_node = LinkedListNode(name)

        # if inserting at index=0, update the head.
        if index == 0:
            new_node.set_next_node(current_ptr)
            self._head = new_node

        # Otherwise, find the location to insert.
        while current_ptr.next_node is not None:

            # Now we're at the index that we want to insert.
            if index == 0:
                break

            index -= 1
            current_ptr = current_ptr.next_node

        # We could not find a valid position, we tried to go to the specified index but it was invalid.
        if index > 0:
            raise InvalidLinkedListIndexError()

        # We should now have two cases -

        # 1. Either the index we want to insert in is at the end of the linked list, in which case set the new tail.
        if current_ptr.next_node is None:
            current_ptr.set_next_node(new_node)
        else:
            # 2. The index we want to insert in is in the middle of the linked list
            next_node = current_ptr.next_node
            new_node.set_next_node(next_node)
            current_ptr.set_next_node(new_node)

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
    def next_node(self):
        """
        :rtype: LinkedListNode or NoneType
        """
        return self._head.next_node

    @property
    def size(self):
        return self._size if self._head is not None else 0