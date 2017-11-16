from linkedlists.linkedlists import SinglyLinkedList
from stacks.stacks import ListStack
from util.linkedlist_util import InvalidLinkedListIndexError
from util.queue_util import QueueInterface, EmptyQueueError
from util.stack_util import EmptyStackError


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
        self._queue.append(item)

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
        self._queue.append(item)

    def dequeue(self):
        try:
            return self._queue.pop_from_beginning()
        except InvalidLinkedListIndexError:
            raise EmptyQueueError()

    def peek(self):
        if self._queue.head is None:
            raise EmptyQueueError()
        return self._queue.head.identifier

    def size(self):
        return self._queue.size


class TwoStacksQueue(QueueInterface):
    """
    An implementation of a queue with two stacks, works by using two stacks and pushing an item into the outgoing stack
    popped from the incoming stack to simulate FIFO behavior. The incoming stack is used as a buffer for enqueue,
    while dequeue does the heavy lifting.

    Enqueue is a constant O(1) operation, but dequeue has worst case O(N) where N is the size of the incoming stack,
    although can be considered to have amortized constant O(1) time as the outgoing queue is only rebalanced from the
    incoming queue if it is empty.
    """

    def __init__(self):
        self._incoming_stack = ListStack()
        self._outgoing_stack = ListStack()

    def enqueue(self, item):
        self._incoming_stack.push(item)

    def dequeue(self):
        self._reorder_stacks()
        try:
            return self._outgoing_stack.pop()
        except EmptyStackError:
            raise EmptyQueueError()

    def _reorder_stacks(self):
        # Reorder the items in the outgoing stack so that the order is reversed, giving FIFO properties.
        # Note here we only reorder the queue of the outgoing stack is empty.
        if self._outgoing_stack.size() == 0:
            while self._incoming_stack.size() > 0:
                self._outgoing_stack.push(self._incoming_stack.pop())

    def peek(self):
        # Reorder the items again as we are not guaranteed that the outgoing stack has anything to return the first item
        self._reorder_stacks()
        try:
            return self._outgoing_stack.peek()
        except EmptyStackError:
            # Stacks in this implementation typically raise an EmptyStackError but we want to catch that and return
            # an empty queue error as it was used to implement a queue.
            raise EmptyQueueError()

    def size(self):
        # Size of the queue must be the size of both stacks.
        return self._outgoing_stack.size() + self._incoming_stack.size()
