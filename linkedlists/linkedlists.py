from util.linkedlist_util import LinkedListNode, InvalidLinkedListIndexError, LinkedListValueMissingError


class SinglyLinkedList:

    def __init__(self, head=None):
        """
        :param head:
        :type head: LinkedListNode or NoneType
        """
        self._head = head
        self._size = 1 if head is not None else 0

    def set_next_node(self, node):
        """
        :param node: the linked list node to be set as the next for this current node.
        :type node: LinkedListNode
        """
        if self._head is None:
            self._size += 1
            self._head = node
            return

        current_ptr = self._head
        while current_ptr.next_node is not None:
            current_ptr = current_ptr.next_node

        current_ptr.set_next_node(node)
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

        # Can't contain the value if there is no head pointer.
        if current_ptr is None:
            raise LinkedListValueMissingError()
        if current_ptr.identifier == name:
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
            if current_ptr.identifier == name:
                current_ptr.set_next_node(current_ptr.next_node.next_node)
                self._size -= 1
                return

            current_ptr = current_ptr.next_node

        # Could not find a value, return a value missing error.
        raise LinkedListValueMissingError()

    def add_to_front(self, name):
        """
        Adds a node to the front.

        :param name: the name of the node to add to the beginning
        """
        self._insert_at_position(name, 0)

    def pop_from_beginning(self):
        """
        Pops the node from the beginning

        :raises:  InvalidLinkedListIndexError
        """
        if self._size == 0:
            raise InvalidLinkedListIndexError()
        return self._pop_at_position(0)

    def append(self, name):
        """
        Appends a node to the end of this linked list.

        :param name: the name of the node to be appended
        :type name: str
        """

        new_node = LinkedListNode(name)

        if self._head is None:
            self._head = new_node
        else:
            current_ptr = self._head

            # Reach the end of this linked list.
            while current_ptr.next_node is not None:
                current_ptr = current_ptr.next_node

            current_ptr.set_next_node(new_node)

        self._size += 1

    def _insert_at_position(self, name, index):
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

            if self._head is None:
                self._head = new_node
            else:
                new_node.set_next_node(current_ptr)
                self._head = new_node
            self._size += 1
            return

        # We traversed past the head node already.
        index -= 1
        prev_ptr = self._head
        current_ptr = self._head.next_node

        # Otherwise, find the location to insert.
        while current_ptr is not None:

            # Now we're at the index that we want to insert.
            if index == 0:
                break

            index -= 1
            prev_ptr = current_ptr
            current_ptr = current_ptr.next_node

        # We could not find a valid position, we tried to go to the specified index but it was invalid.
        if index > 0:
            raise InvalidLinkedListIndexError()

        # We should now have two cases -

        # 1. Either the index we want to insert in is at the end of the linked list, in which case set the new tail.
        if prev_ptr.next_node is None:
            prev_ptr.set_next_node(new_node)
        else:
            # 2. The index we want to insert in is in the middle of the linked list
            next_node = prev_ptr.next_node
            new_node.set_next_node(next_node)
            prev_ptr.set_next_node(new_node)

        # Update size.
        self._size += 1

    def _pop_at_position(self, index):
        """
        Removes a node at a given position.

        :param index:
        :type index: int

        :raise: InvalidLinkedListIndexError
        """

        if index == 0:

            if self._head is None:
                raise InvalidLinkedListIndexError()
            head_data = self._head.identifier
            self._head = self.head.next_node
            self._size -= 1
            return head_data

        # We traversed past the head node already.
        index -= 1
        prev_ptr = self._head
        current_ptr = self._head.next_node

        # Otherwise, find the location to remove.
        while current_ptr is not None:

            # Now we're at the index that we want to remove.
            if index == 0:
                break

            index -= 1
            prev_ptr = current_ptr
            current_ptr = current_ptr.next_node

        # We could not find a valid position, we tried to go to the specified index but it was invalid.
        if index > 0 or current_ptr is None:
            raise InvalidLinkedListIndexError()

        current_data = current_ptr.identifier

        prev_ptr.set_next_node(current_ptr.next_node)

        # Update size.
        self._size -= 1

        return current_data

    def reverse(self):
        current = self._head
        prev = None
        while current is not None:
            next_ptr = current.next_node
            current.set_next_node(prev)
            prev = current
            current = next_ptr
        self._head = prev

    def to_list(self):
        l = []
        current = self._head
        while current is not None:
            l.append(current.identifier)
            current = current.next_node
        return l

    def to_string(self):
        """
        Prints a linked list
        """

        current_ptr = self._head

        if current_ptr is None:
            print "(empty)"

        while current_ptr is not None:
            # Don't include an arrow for the last node.
            arrow = "" if current_ptr.next_node is None else " ->"
            print str(current_ptr.identifier) + arrow,
            current_ptr = current_ptr.next_node
        print ""

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


def get_middle_of_linked_list(linked_list):
    """
    Gets the middle of a linked list
    :param linked_list:
    :type linked_list: SinglyLinkedList
    :return:
    """
    if linked_list.head is None:
        return None

    if linked_list.next_node is None:
        return linked_list.head

    slow = linked_list.head
    fast = linked_list.head

    while fast is not None:
        if fast.next_node is not None:
            slow = slow.next_node
            fast = fast.next_node.next_node
        else:
            break

    return slow


def split_linked_list(linked_list):
    """

    :param linked_list:
    :type linked_list: SinglyLinkedList
    :return:
    """
    if linked_list.head is None:
        return SinglyLinkedList(None), SinglyLinkedList(None)

    # get mid, then split.
    mid = get_middle_of_linked_list(linked_list)
    start = linked_list.head

    if start == mid:
        return SinglyLinkedList(start), SinglyLinkedList(None)

    while start is not None:
        # Iterate through and find when the current pointer's next is the middle, then remove that reference.
        if start.next_node == mid:
            start.set_next_node(None)
            break

        start = start.next_node

    return linked_list, SinglyLinkedList(mid)


def merge_sort_linked_list(linked_list):
    # Base case where the linked list is empty or is of size 1
    if linked_list.head is None or linked_list.head.next_node is None:
        return linked_list

    left_linked_list, right_linked_list = split_linked_list(linked_list)

    left = merge_sort_linked_list(left_linked_list)
    right = merge_sort_linked_list(right_linked_list)

    return combine_linked_list(left, right)


def combine_linked_list(l1, l2):
    """
    Combines two linked lists

    :param l1:
    :type l1: SinglyLinkedList

    :param l2:
    :type l2: SinglyLinkedList

    :return:
    """

    l1_head = l1.head
    l2_head = l2.head

    if l1_head is None:
        return l2
    if l2_head is None:
        return l1

    current_l1_ptr = l1_head
    current_l2_ptr = l2_head

    sorted_linked_list = SinglyLinkedList(None)

    while current_l1_ptr is not None and current_l2_ptr is not None:

        current_l1_val = current_l1_ptr.identifier
        current_l2_val = current_l2_ptr.identifier

        if current_l1_val <= current_l2_val:
            sorted_linked_list.set_next_node(LinkedListNode(current_l1_val))
            current_l1_ptr = current_l1_ptr.next_node
        else:
            sorted_linked_list.set_next_node(LinkedListNode(current_l2_val))
            current_l2_ptr = current_l2_ptr.next_node

    # add endings
    while current_l1_ptr is not None:
        current_l1_val = current_l1_ptr.identifier
        sorted_linked_list.set_next_node(LinkedListNode(current_l1_val))
        current_l1_ptr = current_l1_ptr.next_node

    while current_l2_ptr is not None:
        current_l2_val = current_l2_ptr.identifier
        sorted_linked_list.set_next_node(LinkedListNode(current_l2_val))
        current_l2_ptr = current_l2_ptr.next_node

    return sorted_linked_list
