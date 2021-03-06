from abc import ABCMeta, abstractmethod


class StackInterface(object):
    """
    Provides a basic interface that stacks should implement with Last-in, First-Out behavior.
    """

    __metaclass__ = ABCMeta

    @abstractmethod
    def push(self, item):
        """
        Pushes an item to be at the top of the stack.

        :param item
        """
        raise NotImplementedError("Subclasses must implement the push method.")

    @abstractmethod
    def peek(self):
        """
        Returns the top value in the stack in an read only fashion.

        :raise: EmptyStackError
        """
        raise NotImplementedError("Subclasses must implement the peek method.")

    @abstractmethod
    def pop(self):
        """
        Removes and returns the top value in the stack.

        :raise: EmptyStackError
        """
        raise NotImplementedError("Subclasses must implement the pop method.")

    @abstractmethod
    def size(self):
        """
        Returns the size of the stack.

        :raise: EmptyStackError
        """
        raise NotImplementedError("Subclasses must implement the size method.")


class EmptyStackError(ValueError):
    pass
