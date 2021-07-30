from project.appliances.tv import TV
from project.appliances.fridge import Fridge
from project.appliances.stove import Stove
from project.rooms.room import Room

class OldCouple(Room):
    room_members_count = 2
    room_cost = 10
    apliences = [TV(), TV(), Fridge(), Fridge(), Stove(), Stove()]
    def __init__(self, name: str, pansion_one: float, pansion_two: float):
        super().__init__(name, pansion_one+pansion_two, OldCouple.room_members_count)
        self.calculate_expenses(self.apliences)