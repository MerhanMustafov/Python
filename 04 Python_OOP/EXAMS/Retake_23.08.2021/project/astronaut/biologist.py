from project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    def __init__(self, name):
        super().__init__(name, 70)