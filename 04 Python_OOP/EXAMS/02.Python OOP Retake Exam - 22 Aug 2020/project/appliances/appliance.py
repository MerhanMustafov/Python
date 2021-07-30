

class Appliance:
    """cost: float - passed upon initialization. The cost is for a single day"""
    def __init__(self, cost: float):
        self.cost = cost

    def get_monthly_expense(self):
        return self.cost * 30
