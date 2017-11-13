import unittest

from queues.queues import ListQueue, LinkedListQueue
from util.queue_util import EmptyQueueError


class TestStacks(unittest.TestCase):

    def test_all_queues(self):
        # Runs the following tests for each queue type.
        for queue_type in (ListQueue, LinkedListQueue):
            queue = queue_type()
            self.basic_queue_one_item(queue)
            self.basic_stack_multiple_item(queue)
            self.basic_stack_empty(queue)

    def basic_queue_one_item(self, queue):
        queue = ListQueue()
        queue.enqueue(1)
        actual_peek = queue.peek()
        self.assertTrue(actual_peek == 1)
        self.assertTrue(queue.size() == 1)

        # Remove 1 from the stack so should be empty now.
        actual_dequeue = queue.dequeue()
        self.assertTrue(actual_dequeue == 1)
        self.assertTrue(queue.size() == 0)

    def basic_stack_multiple_item(self, queue):
        queue = ListQueue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        # Remove 3 from the stack
        actual_peek = queue.peek()
        actual_pop = queue.dequeue()
        self.assertTrue(actual_pop == 3)
        self.assertTrue(actual_peek == 3)
        self.assertTrue(queue.size() == 2)

        # Remove 2 from the stack
        actual_peek = queue.peek()
        actual_pop = queue.dequeue()
        self.assertTrue(actual_pop == 2)
        self.assertTrue(actual_peek == 2)
        self.assertTrue(queue.size() == 1)

        # Remove 1 from the stack, which should now be empty
        actual_peek = queue.peek()
        actual_pop = queue.dequeue()
        self.assertTrue(actual_pop == 1)
        self.assertTrue(actual_peek == 1)
        self.assertTrue(queue.size() == 0)

    def basic_stack_empty(self, queue):
        try:
            queue.peek()
            self.assertTrue(False)
        except EmptyQueueError:
            pass

        try:
            queue.dequeue()
            self.assertTrue(False)
        except EmptyQueueError:
            pass

        self.assertTrue(queue.size() == 0)



