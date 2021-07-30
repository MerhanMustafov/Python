from project.appliances.tv import TV
from project.appliances.fridge import Fridge
from project.appliances.stove import Stove
from project.appliances.laptop import Laptop
from project.rooms.room import Room

class YoungCoupleWithChildren(Room):
    initial_room_members_count = 2
    room_cost = 20
    def __init__(self, name: str, salary_one: float, salary_two: float, *children):
        members_count = self.initial_room_members_count + len(children)
        super().__init__(name, salary_one+salary_two, members_count)
        self.children = list(children)
        self.apliences = self.generate_apliences()
        self.calculate_expenses(self.apliences, self.children)
    def generate_apliences(self):
        apliences = []
        for x in range(self.members_count):
            apliences.append(TV())
            apliences.append(Fridge())
            apliences.append(Laptop())
        return apliences


