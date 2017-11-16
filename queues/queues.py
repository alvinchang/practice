from linkedlists.linkedlists import SinglyLinkedList
from util.linkedlist_util import InvalidLinkedListIndexError
from util.queue_util import QueueInterface, EmptyQueueError


class ListQueue(QueueInterface):
    """
    Basic implementation of a queue with a list. Note here that in order to simulate the FIFO behavior, we're using
    a list for simplicity's sake, but a list is probably not the best choice in terms of performance benefits, as we'll
    be removing items from the front, and adding to the back. Adding things in a list implies that items will have to
    be shifted over. A better implementation would be perhaps to use a LinkedList. A python list backing a Stack is not
    too bad as we can always append and pop from the end.
    """

    def __init__(self):
        self._queue = list()

    def enqueue(self, item):
        # This is not so great as we have to copy and shift all elements over to the right once we insert.
        self._queue.insert(0, item)

    def dequeue(self):
        # This is not so great as we have to copy and shift all elements over to the right once we remove.
        if not self._queue:
            raise EmptyQueueError()
        return self._queue.pop(0)

    def peek(self):
        if not self._queue:
            raise EmptyQueueError()
        return self._queue[0]

    def size(self):
        return len(self._queue)


class LinkedListQueue(QueueInterface):
    """
    An implementation of a queue that uses a linked list, which would have O(1) add to front, and O(1) remove from end
    to simulate a FIFO queue with better performance than a python list.
    """

    def __init__(self):
        self._queue = SinglyLinkedList()

    def enqueue(self, item):
        self._queue.add_to_front(item)

    def dequeue(self):
        try:
            return self._queue.pop_from_end()
        except InvalidLinkedListIndexError:
            raise EmptyQueueError()

    def peek(self):
        if self._queue.head is None:
            raise EmptyQueueError()
        return self._queue.head.identifier

    def size(self):
        return self._queue.size
