from abc import ABCMeta


class Node(object):

    # All nodes have an identifier as denoted by 'name'

    __metaclass__ = ABCMeta

    def __init__(self, name):
        """
        :param name: expected int or str identifier for these purposes.
        :type name: Any
        """
        self._name = name

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
    def name(self):
        return self._name
