from project.appliances.tv import TV
from project.appliances.fridge import Fridge
from project.appliances.stove import Stove
from project.rooms.room import Room

class OldCouple(Room):
    members_count = 2
    def __init__(self, family_name, pension_one, pension_two):
        super().__init__(family_name, pension_one + pension_two, 2)
        self.room_cost = 15
        self.appliances = [TV(), Fridge(), Stove()] * 2

        self.calculate_expenses(self.appliances)

#
# from project.appliances.fridge import Fridge
# from project.appliances.stove import Stove
# from project.appliances.tv import TV
# from project.rooms.room import Room
#
#
# class OldCouple(Room):
#     def __init__(self, family_name, pension_one, pension_two):
#         super().__init__(family_name, pension_one + pension_two, 2)
#         self.room_cost = 15
#         self.appliances = [TV(), Fridge(), Stove()] * 2
#         self.calculate_expenses(self.appliances)