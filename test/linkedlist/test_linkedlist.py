import unittest

from util.linkedlist_util import generate_linked_list


class TestLinkedList(unittest.TestCase):

    def test_basic_linked_list(self):
        node_list = ["A", "B", "C"]
        linked_list = generate_linked_list(node_list)

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
        linked_list = generate_linked_list(node_list)

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

    def test_basic_linked_list_remove_from_head(self):
        node_list = ["A", "B", "C"]
        linked_list = generate_linked_list(node_list)

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

    def test_basic_linked_list_remove_from_mid(self):
        node_list = ["A", "B", "C"]
        linked_list = generate_linked_list(node_list)

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

    def test_basic_linked_list_remove_from_end(self):
        node_list = ["A", "B", "C"]
        linked_list = generate_linked_list(node_list)

        last_node_to_remove = node_list.pop()

        print node_list

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














