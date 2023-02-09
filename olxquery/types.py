from abc import ABC, abstractmethod


class Location(ABC):
    @abstractmethod
    def __init__(self):
        return NotImplementedError


class Category(ABC):
    @abstractmethod
    def __init__(self):
        return NotImplementedError
