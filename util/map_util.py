from abc import ABCMeta, abstractmethod, abstractproperty


class MapInterface:

    __metaclass__ = ABCMeta

    @abstractmethod
    def get(self, key):
        raise NotImplementedError("Subclasses must implement the get method.")

    @abstractmethod
    def put(self, key, value):
        raise NotImplementedError("Subclasses must implement the put method.")

    @abstractproperty
    def size(self):
        raise NotImplementedError("Subclasses must implement the size property.")

