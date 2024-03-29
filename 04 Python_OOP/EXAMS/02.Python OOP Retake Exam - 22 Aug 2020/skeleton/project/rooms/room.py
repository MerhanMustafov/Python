from project.appliances.appliance import Appliance
from project.people.child import Child


class Room:
    def __init__(self, name, budget, members_count):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.expenses = 0

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self.__expenses = value

    def calculate_expenses(self, *args):
        result = 0
        for list_el in args:
            for el in list_el:
                if isinstance(el, Appliance):
                    result += el.get_monthly_expense()
                elif isinstance(el, Child):
                    result += el.cost * 30
        self.expenses = result

# from project.appliances.appliance import Appliance
# from project.people.child import Child
#
#
# class Room:
#     def __init__(self, name, budget, members_count):
#         self.family_name = name
#         self.budget = budget
#         self.members_count = members_count
#         self.children = []
#         # TODO think about this one
#         self.expenses = 0
#
#     @property
#     def expenses(self):
#         return self.__expenses
#
#     @expenses.setter
#     def expenses(self, value):
#         if value < 0:
#             raise ValueError("Expenses cannot "
#                              "be negative")
#         self.__expenses = value
#
#     def calculate_expenses(self, *args):
#         total_expenses = 0
#         for list_el in args:
#             for el in list_el:
#                 # TODO implement get_monthly_expense in Child class
#                 if isinstance(el, Appliance):
#                     total_expenses += el.get_monthly_expense()
#                 elif isinstance(el, Child):
#                     total_expenses += el.cost * 30
#         self.expenses = total_expenses