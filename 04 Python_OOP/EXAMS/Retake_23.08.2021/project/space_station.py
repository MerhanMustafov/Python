from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()

        self.successful = 0
        self.unsuccessful = 0
    def add_astronaut(self, astronaut_type: str, name: str):
        if astronaut_type == "Biologist" or\
            astronaut_type == "Geodesist" or\
            astronaut_type == "Meteorologist":

            astronaut = None
            if astronaut_type == "Biologist":
                astronaut = Biologist(name)
            elif astronaut_type == "Geodesist":
                astronaut = Geodesist(name)
            elif astronaut_type == "Meteorologist":
                astronaut = Meteorologist(name)

            if self.astronaut_repository.find_by_name(name):
                return f"{name} is already added."
            self.astronaut_repository.add(astronaut)
            return f"Successfully added {astronaut_type}: {name}."

        raise Exception("Astronaut type is not valid!")

    def add_planet(self, name, items: str):

        if self.planet_repository.find_by_name(name):
            return f"{name} is already added."
        items = items.split(", ")
        planet = Planet(name)
        planet.items = items
        self.planet_repository.add(planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name):
        if not self.astronaut_repository.find_by_name(name):
            raise Exception(f"Astronaut {name} doesn't exists!")
        astronaut = self.astronaut_repository.find_by_name(name)
        self.astronaut_repository.remove(astronaut)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.oxygen += 10

    def send_on_mission(self, planet_name: str):
        if not self.planet_repository.find_by_name(planet_name):
            raise Exception("Invalid planet name!")

        suitable_for_mission = [a for a in self.astronaut_repository.astronauts if a.oxygen > 30]

        if not suitable_for_mission:
            raise Exception("You need at least one astronaut to explore the planet!")
        suitable = None
        if len(suitable_for_mission) >= 5:
            suitable = suitable_for_mission.sort(key=lambda x: x.oxygen, reverse=True)[:5]
        else:
            suitable = suitable_for_mission.sort(key=lambda x: x.oxygen, reverse=True)



        for astr in suitable:
            for i in range(len(self.planet_repository.planets.items) - 1, -1, -1):

                astr.backpack.append(self.planet_repository.planets.items.pop())
                astr.breathe()
                if astr.oxygen <= 0:
                    break
            if not self.planet_repository.planets.items:
                break
        if not self.planet_repository.planets.items:
            self.successful += 1
            return f"Planet: {planet_name} was explored. {len(suitable)} astronauts participated in collecting items."

        else:
            self.unsuccessful += 1
            return f"Mission is not completed."


    def report(self):
        result = f"{self.successful} successful missions!\n"
        result += f"{self.unsuccessful} missions were not completed!\n"
        result += f"Astronauts' info:\n"
        for a in self.astronaut_repository.astronauts:
            result += f"Name: {a.name}\n"
            result += f"Oxygen: {a.oxygen}\n"
            if a.backpack:
                result += f"Backpack items: {', '.join(self.astronaut_repository.astronauts.backpack)}\n"
            else:
                # result += f"Backpack items: {'none'}\n"
                result += "none\n"

        return result[:-1]


