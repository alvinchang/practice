from util.stack_util import StackInterface, EmptyStackError


class ListStack(StackInterface):
    """
    Here we use a python list to back the stack, appending and popping from the end, we could also use a linked list.
    """
    def __init__(self):
        self._stack = []

    def pop(self):
        if not self._stack:
            raise EmptyStackError()
        return self._stack.pop()

    def push(self, item):
        self._stack.append(item)

    def size(self):
        return len(self._stack)

    def peek(self):
        if not self._stack:
            raise EmptyStackError
        return self._stack[-1]

