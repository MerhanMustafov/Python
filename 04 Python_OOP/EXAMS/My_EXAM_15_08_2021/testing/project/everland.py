class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room):#obj
        self.rooms.append(room)


    def get_monthly_consumptions(self):
        total_consumption = 0
        for room in self.rooms:
            total_consumption += room.expenses + room.room_cost

        return f"Monthly consumtions: {total_consumption:.2f}$."

    def pay(self):
        rooms_info = []
        for room in self.rooms:

            if room.budget >= room.expenses + room.room_cost:
                paid = room.expenses + room.room_cost
                left_budget = room.budget - paid
                room.budget -= paid
                rooms_info.append(f"{room.family_name} paid"
                                  f" {(paid):.2f}$ and have"
                                  f" {left_budget:.2f}$ left.")

            else:
                rooms_info.append(f"{room.family_name} does not have enough"
                                       f" budget and must leave the hotel.")
                self.rooms.remove(room)
        return "\n".join(rooms_info)

    def status(self):
        result = f"Total population: {sum([room.members_count for room in self.rooms])}\n"
        for room in self.rooms:
            room_name = room.family_name
            members = room.members_count
            current_budget = room.budget
            expenses = room.expenses
            result += f"{room_name} with {members} members. Budget: {current_budget:.2f}$, Expenses: {expenses:.2f}$\n"

            child_count = 1
            for child in room.children:
                result += f"--- Child {child_count} monthly cost: {(child.cost * 30):.2f}$\n"
                child_count += 1

            appliances_monthly_cost = sum([ap.cost * 30 for ap in room.appliances])
            result += f"--- Appliances monthly cost: {appliances_monthly_cost:.2f}$\n"

        return result

