from abc import ABC, abstractmethod


class Supply(ABC):
    def __init__(self, needs_increase):
        self.__needs_increase = needs_increase

    @property
    def needs_increase(self):
        return self.__needs_increase

    @needs_increase.setter
    def needs_increase(self, value):
        if value < 0:
            raise ValueError("Needs increase cannot be less than zero.")
        self.__needs_increase = value

    # TODO think if this should be marked with @abstractmethod
    @abstractmethod
    def apply(self, survivor):
        pass