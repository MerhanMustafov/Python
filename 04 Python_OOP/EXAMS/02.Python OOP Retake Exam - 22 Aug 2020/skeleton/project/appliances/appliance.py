class Appliance:
    def __init__(self, cost):
        self.cost = cost# cost for a
                        # single day

    def get_monthly_expense(self):
        return self.cost * 30
#
# class Appliance:
#     def __init__(self, cost):
#         # for a single day
#         self.cost = cost
#
#     def get_monthly_expense(self):
#         return self.cost * 30