from abc import ABC, abstractmethod

class Character(ABC):

    @abstractmethod
    def _attack(self):
        pass

    @abstractmethod
    def _move(self):
        pass

    @abstractmethod
    def _collide(self):
        pass