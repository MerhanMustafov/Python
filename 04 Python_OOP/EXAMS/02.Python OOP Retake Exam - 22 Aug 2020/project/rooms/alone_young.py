from project.appliances.tv import TV
from project.rooms.room import Room

class AloneYoung(Room):
    room_members_count = 1
    room_cost = 10
    apliences = [TV()]
    def __init__(self, name: str, salary: float):
        super().__init__(name, salary,AloneYoung.room_members_count)
        self.calculate_expenses(self.apliences)