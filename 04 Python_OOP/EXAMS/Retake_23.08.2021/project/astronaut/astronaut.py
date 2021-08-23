from abc import ABC, abstractmethod


class Astronaut(ABC):
    @abstractmethod
    def __init__(self, name, oxygen):
        self.name = name
        self.oxygen = oxygen

        self.backpack = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "" or value == " ":
            raise ValueError("Astronaut name cannot be empty string or whitespace!")

        self.__name = value


    def breathe(self):
        if self.__class__.__name__ == "Biologist":
            self.oxygen -= 5
        elif self.__class__.__name__ == "Geodesist":
            self.oxygen -= 10
        elif self.__class__.__name__ == "Meteorologist":
            self.oxygen -= 15

    def increase_oxygen(self, amount):
        self.oxygen += amount

