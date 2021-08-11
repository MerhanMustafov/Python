from project.medicine.medicine import Medicine
from project.supply.supply import Supply


class Bunker(Supply, Medicine):
    def __init__(self, __needs_increase, __health_increase):
        super().__init__(__needs_increase)
        super().__init__(__health_increase)
        self.survivors = []#all the survivors (objects)
        self.supplies = []#all the supplies (objects)
        self.medicine = []#all the medicine (objects)
        self.__food = []
        self.__water = []
        self.__painkillers = []
        self.__salves = []
    @property
    def food(self):
        if [sup for sup in self.supplies if sup.__class__.__name__ == "FoodSupply"][0]:
            return [sup for sup in self.supplies if sup.__class__.__name__ == "FoodSupply"]
        raise IndexError("There are no food supplies left!")

    @property
    def water(self):
        if [sup for sup in self.supplies if sup.__class__.__name__ == "WaterSupply"][0]:
            return [sup for sup in self.supplies if sup.__class__.__name__ == "WaterSupply"]
        raise IndexError("There are no water supplies left!")

    @property
    def painkillers(self):
        if [med for med in self.medicine if med.__class__.__name__ == "Painkiller"][0]:
            return [med for med in self.medicine if med.__class__.__name__ == "Painkiller"]
        raise IndexError("There are no painkillers left!")

    @property
    def salves(self):
        if [med for med in self.medicine if med.__class__.__name__ == "Painkiller"][0]:
            return [med for med in self.medicine if med.__class__.__name__ == "Painkiller"]
        raise IndexError("There are no salves left!")



    def add_survivor(self, survivor):#obj
        if survivor in self.survivors:
            raise ValueError(f"Survivor with name {survivor.name} already exists.")
        self.survivors.append(survivor)
    def add_supply(self, supply):#obj
        self.supplies.append(supply)
    def add_medicine(self, medicine):#obj
        self.medicine.append(medicine)
    def heal(self, survivor, medicine_type):
        if survivor.needs_healing:
            for med in self.medicine[::-1]:
                if isinstance(med, medicine_type):
                    survivor.apply()
                    return f"{survivor.name} healed successfully with {medicine_type}"

    def sustain(self, survivor, sustenance_type):
        if survivor.needs_sustenance:
            for s in self.supplies[::-1]:
                if isinstance(s, sustenance_type):
                    survivor.apply()
                    return f"{survivor.name} sustained successfully with {sustenance_type}"



    def next_day(self):
        for sur in self.survivors:
            sur.needs -= sur.age * 2

        for s in self.survivors:
            if s.needs + 20 > 100:
                s.needs = 100
            else:
                s.needs += 20
            if s.needs + 40 > 100:
                s.needs = 100
            else:
                s.needs += 40






