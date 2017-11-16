from abc import ABCMeta


class Node(object):

    # All nodes have an identifier as denoted by 'name'

    __metaclass__ = ABCMeta

    def __init__(self, identifier):
        """
        :param identifier: expected int or str identifier for these purposes.
        :type identifier: Any
        """
        self._identifier = identifier

    def __eq__(self, other):
        if isinstance(self, type(other)):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __ne__(self, other):
        eq = self.__eq__(other)
        if eq is not NotImplemented:
            return not self.__eq__(other)
        return NotImplemented

    def __hash__(self):
        return tuple(sorted(self.__dict__.items()))

    @property
    def identifier(self):
        return self._identifier
