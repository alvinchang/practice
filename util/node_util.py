from abc import ABCMeta


class Node:

    # All nodes have an identifier as denoted by 'name'

    __metaclass__ = ABCMeta

    def __init__(self, name):
        """
        :param name: expected int or str identifier for these purposes.
        :type name: int or str
        """
        self._name = name

    @property
    def name(self):
        return self._name


