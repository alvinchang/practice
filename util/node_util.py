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


class KVPair:
    """
    This class encapsulates what it means to be a key-value pair, namely just has a key and a value identifier, to be
    used in map implementations.
    """

    def __init__(self, key, value):
        self._key = key
        self._value = value

    def set_value(self, value):
        self._value = value

    @property
    def key(self):
        return self._key

    @property
    def value(self):
        return self._value