import unittest

from stacks.stacks import ListStack
from util.stack_util import EmptyStackError


class TestStacks(unittest.TestCase):

    def test_basic_stack_one_item(self):
        stack = ListStack()
        stack.push(1)
        actual_peek = stack.peek()
        self.assertTrue(actual_peek == 1)
        self.assertTrue(stack.size() == 1)

        # Remove 1 from the stack so should be empty now.
        actual_pop = stack.pop()
        self.assertTrue(actual_pop == 1)
        self.assertTrue(stack.size() == 0)

    def test_basic_stack_multiple_item(self):
        stack = ListStack()
        stack.push(1)
        stack.push(2)
        stack.push(3)

        # Remove 3 from the stack
        actual_peek = stack.peek()
        actual_pop = stack.pop()
        self.assertTrue(actual_pop == 3)
        self.assertTrue(actual_peek == 3)
        self.assertTrue(stack.size() == 2)

        # Remove 2 from the stack
        actual_peek = stack.peek()
        actual_pop = stack.pop()
        self.assertTrue(actual_pop == 2)
        self.assertTrue(actual_peek == 2)
        self.assertTrue(stack.size() == 1)

        # Remove 1 from the stack, which should now be empty
        actual_peek = stack.peek()
        actual_pop = stack.pop()
        self.assertTrue(actual_pop == 1)
        self.assertTrue(actual_peek == 1)
        self.assertTrue(stack.size() == 0)

    def test_basic_stack_empty(self):
        stack = ListStack()
        try:
            stack.peek()
            self.assertTrue(False)
        except EmptyStackError:
            pass

        try:
            stack.pop()
            self.assertTrue(False)
        except EmptyStackError:
            pass

        self.assertTrue(stack.size() == 0)



