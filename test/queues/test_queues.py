import unittest

from queues.queues import ListQueue, LinkedListQueue, TwoStacksQueue
from util.queue_util import EmptyQueueError


class TestQueues(unittest.TestCase):

    def test_all_queues(self):
        # Runs the following tests for each queue type.
        for queue_type in (ListQueue, LinkedListQueue, TwoStacksQueue):
            self.basic_queue_one_item(queue_type)
            self.basic_queue_multiple_item(queue_type)
            self.basic_queue_empty(queue_type)

    def basic_queue_one_item(self, queue_type):
        queue = queue_type()
        queue.enqueue(1)
        actual_peek = queue.peek()
        self.assertTrue(actual_peek == 1)
        self.assertTrue(queue.size() == 1)

        # Remove 1 from the queue so should be empty now.
        actual_dequeue = queue.dequeue()
        self.assertTrue(actual_dequeue == 1)
        self.assertTrue(queue.size() == 0)

    def basic_queue_multiple_item(self, queue_type):
        queue = queue_type()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        # Remove 3 from the queue
        actual_peek = queue.peek()
        actual_pop = queue.dequeue()
        self.assertTrue(actual_pop == 1)
        self.assertTrue(actual_peek == 1)
        self.assertTrue(queue.size() == 2)

        # Remove 2 from the queue
        actual_peek = queue.peek()
        actual_pop = queue.dequeue()
        self.assertTrue(actual_pop == 2)
        self.assertTrue(actual_peek == 2)
        self.assertTrue(queue.size() == 1)

        # Remove 1 from the queue, which should now be empty
        actual_peek = queue.peek()
        actual_pop = queue.dequeue()
        self.assertTrue(actual_pop == 3)
        self.assertTrue(actual_peek == 3)
        self.assertTrue(queue.size() == 0)

    def basic_queue_empty(self, queue_type):
        queue = queue_type()
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



