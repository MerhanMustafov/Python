from project.supply.food_supply import FoodSupply
from project.supply.water_supply import WaterSupply
from project.survivor import Survivor


class Bunker:
    def __init__(self):
        self.survivors = []
        self.supplies = []
        self.medicine = []

    @property
    def food(self):
        f = [f for f in self.supplies if f.__class__.__name__ == "FoodSupply"]
        if not f:
            raise IndexError("There are no food supplies left!")
        return list(f)

    @property
    def water(self):
        w = [w for w in self.supplies if w.__class__.__name__ == "WaterSupply"]
        if not w:
            raise IndexError("There are no water supplies left!")
        return list(w)

    @property
    def painkillers(self):
        pk = [p for p in self.medicine if p.__class__.__name__ == "Painkiller"]
        if not pk:
            raise IndexError("There are no painkillers left!")
        return list(pk)

    @property
    def salves(self):
        s = [s for s in self.medicine if s.__class__.__name__ == "Salve"]
        if not s:
            raise IndexError("There are no salves left!")
        return list(s)

    def add_survivor(self, survivor):
        for s in self.survivors:
            if s.name == survivor.name:
        # if survivor in self.survivors:
                raise ValueError(f"Survivor with name {survivor.name} already exists.")
        self.survivors.append(survivor)

    def add_supply(self, supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine):
        self.medicine.append(medicine)

    def heal(self, survivor: Survivor, medicine_type):
        if survivor.needs_healing:
            medicine = [m for m in self.medicine if m.__class__.__name__ == medicine_type][-1]
            self.medicine.remove(medicine)
            medicine.apply(survivor)
            return f"{survivor.name} healed successfully with {medicine_type}"

    def sustain(self, survivor, sustenance_type):
        if survivor.needs_sustenance:
            supply = [s for s in self.supplies if s.__class__.__name__ == sustenance_type][-1]
            self.supplies.remove(supply)
            supply.apply(survivor)
            return f"{survivor.name} sustained successfully with {sustenance_type}"

    def next_day(self):
        for survivor in self.survivors:
            survivor.needs -= survivor.age * 2

        food = "FoodSupply"
        water = "WaterSupply"
        for survivor in self.survivors:
            self.sustain(survivor, food)
            self.sustain(survivor, water)

