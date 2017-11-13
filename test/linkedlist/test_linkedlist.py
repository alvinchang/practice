import unittest

from linkedlists.linkedlists import LinkedList
from util.linkedlist_util import LinkedListNode, InvalidLinkedListIndexError


class TestLinkedList(unittest.TestCase):

    def test_basic_linked_list(self):
        node_list = ["A", "B", "C"]
        linked_list = TestLinkedList.generate_linked_list(node_list)

        node_index = 0
        current_ptr = linked_list.head
        while current_ptr.next_node is not None:
            current_node_name = current_ptr.name

            # Check that the current node has the correct name.
            self.assertTrue(current_node_name == node_list[node_index])

            current_ptr = current_ptr.next_node
            node_index += 1

    def test_basic_linked_list_append(self):
        node_list = ["A", "B", "C"]
        linked_list = TestLinkedList.generate_linked_list(node_list)

        # Add "D" to the end
        linked_list.append("D")
        node_index = 0
        current_ptr = linked_list.head
        node_list.extend("D")
        while current_ptr.next_node is not None:
            current_node_name = current_ptr.name

            # Check that the current node has the correct name.
            self.assertTrue(current_node_name == node_list[node_index])

            current_ptr = current_ptr.next_node
            node_index += 1

    def test_basic_linked_list_remove_node_from_head(self):
        node_list = ["A", "B", "C"]
        linked_list = TestLinkedList.generate_linked_list(node_list)

        first_node_to_remove = node_list.pop(0)

        linked_list.remove_node_with_name(first_node_to_remove)

        node_index = 0
        current_ptr = linked_list.head

        while current_ptr.next_node is not None:
            current_node_name = current_ptr.name

            # Check that the current node has the correct name.
            self.assertTrue(current_node_name == node_list[node_index])

            current_ptr = current_ptr.next_node
            node_index += 1

    def test_basic_linked_list_remove_node_from_mid(self):
        node_list = ["A", "B", "C"]
        linked_list = TestLinkedList.generate_linked_list(node_list)

        middle_node_to_remove = node_list.pop(1)

        print node_list

        linked_list.remove_node_with_name(middle_node_to_remove)

        linked_list.to_string()

        node_index = 0
        current_ptr = linked_list.head

        while current_ptr.next_node is not None:
            current_node_name = current_ptr.name

            # Check that the current node has the correct name.
            self.assertTrue(current_node_name == node_list[node_index])

            current_ptr = current_ptr.next_node
            node_index += 1

    def test_basic_linked_list_remove_node_from_end(self):
        node_list = ["A", "B", "C"]
        linked_list = TestLinkedList.generate_linked_list(node_list)

        last_node_to_remove = node_list.pop()

        linked_list.remove_node_with_name(last_node_to_remove)

        linked_list.to_string()

        node_index = 0
        current_ptr = linked_list.head

        while current_ptr.next_node is not None:
            current_node_name = current_ptr.name

            # Check that the current node has the correct name.
            self.assertTrue(current_node_name == node_list[node_index])

            current_ptr = current_ptr.next_node
            node_index += 1

    def test_basic_linked_list_insert_at_head(self):
        node_list = ["A", "B", "C"]
        linked_list = TestLinkedList.generate_linked_list(node_list)

        node_list.insert(0, "D")
        linked_list._insert_at_position("D", 0)

        node_index = 0
        current_ptr = linked_list.head

        while current_ptr.next_node is not None:
            current_node_name = current_ptr.name

            # Check that the current node has the correct name.
            self.assertTrue(current_node_name == node_list[node_index])

            current_ptr = current_ptr.next_node
            node_index += 1

    def test_basic_linked_list_insert_at_middle(self):
        node_list = ["A", "B", "C"]
        linked_list = TestLinkedList.generate_linked_list(node_list)

        node_list.insert(1, "D")
        linked_list._insert_at_position("D", 1)

        node_index = 0
        current_ptr = linked_list.head

        while current_ptr.next_node is not None:
            current_node_name = current_ptr.name

            # Check that the current node has the correct name.
            self.assertTrue(current_node_name == node_list[node_index])

            current_ptr = current_ptr.next_node
            node_index += 1

    def test_basic_linked_list_insert_at_middle_2(self):
        node_list = ["A", "B", "C"]
        linked_list = TestLinkedList.generate_linked_list(node_list)

        node_list.insert(2, "D")
        linked_list._insert_at_position("D", 2)

        node_index = 0
        current_ptr = linked_list.head

        while current_ptr.next_node is not None:
            current_node_name = current_ptr.name

            # Check that the current node has the correct name.
            self.assertTrue(current_node_name == node_list[node_index])

            current_ptr = current_ptr.next_node
            node_index += 1

    def test_basic_linked_list_insert_at_end(self):
        node_list = ["A", "B", "C"]
        linked_list = TestLinkedList.generate_linked_list(node_list)

        linked_list._insert_at_position("D", 3)

        linked_list.to_string()

        node_index = 0
        current_ptr = linked_list.head

        while current_ptr.next_node is not None:
            current_node_name = current_ptr.name

            # Check that the current node has the correct name.
            self.assertTrue(current_node_name == node_list[node_index])

            current_ptr = current_ptr.next_node
            node_index += 1

    def test_basic_linked_list_insert_at_invalid(self):
        node_list = ["A", "B", "C"]
        linked_list = TestLinkedList.generate_linked_list(node_list)

        try:
            linked_list._insert_at_position("D", 4)
            self.assertTrue(False)
        except InvalidLinkedListIndexError:
            pass

    def test_basic_linked_list_remove_from_beginning(self):
        node_list = ["A", "B", "C"]
        linked_list = TestLinkedList.generate_linked_list(node_list)

        linked_list._pop_at_position(0)
        node_list.pop(0)

        linked_list.to_string()

        node_index = 0
        current_ptr = linked_list.head

        while current_ptr.next_node is not None:
            current_node_name = current_ptr.name

            # Check that the current node has the correct name.
            self.assertTrue(current_node_name == node_list[node_index])

            current_ptr = current_ptr.next_node
            node_index += 1

    def test_basic_linked_list_remove_from_middle(self):
        node_list = ["A", "B", "C"]
        linked_list = TestLinkedList.generate_linked_list(node_list)

        linked_list._pop_at_position(1)
        node_list.pop(1)

        linked_list.to_string()

        node_index = 0
        current_ptr = linked_list.head

        while current_ptr.next_node is not None:
            current_node_name = current_ptr.name

            # Check that the current node has the correct name.
            self.assertTrue(current_node_name == node_list[node_index])

            current_ptr = current_ptr.next_node
            node_index += 1

    def test_basic_linked_list_remove_from_end(self):
        node_list = ["A", "B", "C"]
        linked_list = TestLinkedList.generate_linked_list(node_list)

        linked_list._pop_at_position(2)
        node_list.pop(2)

        linked_list.to_string()

        node_index = 0
        current_ptr = linked_list.head

        while current_ptr.next_node is not None:
            current_node_name = current_ptr.name

            # Check that the current node has the correct name.
            self.assertTrue(current_node_name == node_list[node_index])

            current_ptr = current_ptr.next_node
            node_index += 1

    def test_basic_linked_list_remove_at_invalid(self):
        node_list = ["A", "B", "C"]
        linked_list = TestLinkedList.generate_linked_list(node_list)

        try:
            linked_list._pop_at_position(3)
            self.assertTrue(False)
        except InvalidLinkedListIndexError:
            pass

    @staticmethod
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
        linked_list = LinkedList(LinkedListNode(head_node_name))
        for _i in xrange(1, len(node_list)):
            node_name = node_list[_i]
            node = LinkedListNode(node_name)
            linked_list.set_next_node(node)

        return linked_list



