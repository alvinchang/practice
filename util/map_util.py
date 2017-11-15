from abc import ABCMeta, abstractmethod

from util.node_util import Node


class MapInterface(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def get(self, key):
        """
        Gets the value from a specified key. Returns None if it did not exist.

        :param key:
        :return:
        """
        raise NotImplementedError("Subclasses must implement the get function.")

    @abstractmethod
    def put(self, key, value):
        """
        Stores the value from a specified key, and overwrites the value if the key already exists.

        :param key:
        :param value:
        :return:
        """
        raise NotImplementedError("Subclasses must implement the put function.")

    @abstractmethod
    def hash(self, key):
        """
        Return the hash key for which to store and retrieve kv pairs.
        :param key:
        :return:
        """

        raise NotImplementedError("Subclasses must implement the hash function.")

    @abstractmethod
    def remove(self, key):
        """
        Removes the key if it exists, raises a ValueError if it did not exist.
        :param key:
        :raises: ValueError
        """
        raise NotImplementedError("Subclasses must implement the remove function.")


class ValueMissingError(ValueError):
    pass


class Map(MapInterface):

    __metaclass__ = ABCMeta

    def __init__(self, chain_type, size):
        """
        :param chain_type: the type of data structure that you want to chain with. The value will be stored as
        tuple (key, value) pairs in the chain type.
        :type chain_type:

        :param size:
        :type size: int
        """
        self._chain_map = {_i: chain_type() for _i in xrange(0, size)}
        self._size = size

    def hash(self, key):
        """
        Simple hash function that returns hash(key) modded by the size.

        :param key:
        :return:
        """
        return hash(key) % self._size

    @property
    def size(self):
        return self._size

    @property
    def chain_map(self):
        return self._chain_map


class KVPair(Node):
    """
    This class encapsulates what it means to be a key-value pair, namely just has a key and a value identifier, to be
    used in map implementations.
    """

    def __init__(self, key, value):
        self._key = key
        self._value = value
        kv_pair = (key, value)
        super(KVPair, self).__init__(kv_pair)

    @property
    def key(self):
        return self._key

    @property
    def value(self):
        return self._value

