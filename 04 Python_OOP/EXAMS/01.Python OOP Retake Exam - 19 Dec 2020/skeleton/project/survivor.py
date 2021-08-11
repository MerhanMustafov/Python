from project.supply.supply import Supply


class Survivor(Supply):
    def __init__(self, __needs_increase,name, age):
        super().__init__(__needs_increase)
        self.__name = name
        self.__age = age
        self.__health = 100
        self.__needs = 100
        self.__needs_sustenance = False
        self.__needs_healing = False

    def apply(self, survivor):
        if self.__health + self.__needs_increase > 100:
            self.__health = 100
        else:
            self.__health += self.__needs_increase

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Name not valid!")
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age not valid!")
        self.__age = value

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            raise ValueError("Health not valid!")

    @property
    def needs(self):
        return self.__needs

    @health.setter
    def health(self, value):
        if value < 0:
            raise ValueError("Needs not valid!")
        self.__needs = value

    @property
    def needs_sustenance(self):
        if self.__needs < 100:
            return True

    @property
    def needs_healing(self):
        if self.__health < 100:
            return True

