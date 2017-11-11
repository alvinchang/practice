from abc import ABCMeta, abstractmethod


class QueueInterface(object):

    """
    Provides a basic interface that Queues should implement with First-in, First-Out behavior.
    """

    __metaclass__ = ABCMeta

    @abstractmethod
    def enqueue(self, item):
        """
        Puts an item to be at the end of the queue.

        :param item:
        """
        raise NotImplementedError("Subclasses must implement the enqueue method.")

    @abstractmethod
    def dequeue(self):
        """
        Removes and returns item at the start of the queue.

        :raises:EmptyQueueError

        """
        raise NotImplementedError("Subclasses must implement the dequeue method.")

    @abstractmethod
    def peek(self):
        """
        Returns item at the start of the queue in a read only fashion.

        :raises:EmptyQueueError

        """
        raise NotImplementedError("Subclasses must implement the peek method.")

    @abstractmethod
    def size(self):
        """
        Returns the size of the queue.
        """
        raise NotImplementedError("Subclasses must implement the size method.")


class EmptyQueueError(ValueError):
    pass



