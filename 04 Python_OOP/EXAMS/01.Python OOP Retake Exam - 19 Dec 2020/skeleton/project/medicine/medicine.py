from abc import ABC, abstractmethod



class Medicine(ABC):
    def __init__(self, health_increase):
        self.__health_increase = health_increase

    @property
    def health_increase(self):
        return self.__health_increase

    @health_increase.setter
    def health_increase(self, value):
        if value < 0:
            raise ValueError("Health increase cannot be less than zero.")
        self.__health_increase = value

        # TODO think if this should be marked with @abstractmethod

    @abstractmethod
    def apply(self, survivor):
        """Method should increase the needs property of the
         given survivor with the supply's needs_increase value"""
        # survivor.health += self.__health_increase
        pass