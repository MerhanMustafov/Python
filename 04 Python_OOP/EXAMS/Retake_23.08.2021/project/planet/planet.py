class Planet:

    def __init__(self, name):
        self.name = name

        #an empty list of strings holding
        # each item that could be found on that planet
        self.items = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "" or value == " ":
            raise ValueError("Planet name cannot be empty string or whitespace!")

        self.__name = value




