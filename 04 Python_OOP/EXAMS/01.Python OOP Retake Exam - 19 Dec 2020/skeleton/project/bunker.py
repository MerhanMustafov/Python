class Bunker:
    def __init__(self):
        self.survivors = []#all the survivors (objects)
        self.supplies = []#all the supplies (objects)
        self.medicine = []#all the medicine (objects)

    @property
    def food(self):
        food_s = [sup for sup in self.supplies if sup.__class__.__name__ == "FoodSupply"]
        if food_s:
            return food_s
        else:
            raise IndexError(f"There are no food supplies left!")
    @property
    def water(self):
        water_sup = [sup for sup in self.supplies if sup.__class__.__name__ == "WaterSupply"]
        if water_sup:
            return water_sup
        else:
            raise IndexError(f"There are no water supplies left!")
    @property
    def painkillers(self):
        painkiller = [m for m in self.medicine if m.__class__.__name__ == "Painkiller"]
        if painkiller:
            return painkiller
        else:
            raise IndexError(f"There are no painkillers left!")
    @property
    def salves(self):
        salves = [m for m in self.medicine if m.__class__.__name__ == "Salve"]
        if salves:
            return salves
        else:
            raise IndexError(f"There are no salves left!")


    def add_survivor(self, survivor):#obj
        if survivor in self.survivors:
            raise ValueError(f"Survivor with name {survivor.name} already exists.")
        self.survivors.append(survivor)
    def add_supply(self, supply):#obj
        self.supplies.append(supply)
    def add_medicine(self, medicine):#obj
        self.medicine.append(medicine)
    def heal(self, survivor, medicine_type):
        to_remove_med = [m for m in self.medicine if m.__class__.__name__ == medicine_type][-1]

        if survivor.needs_healing:
            self.medicine.remove(to_remove_med)
            to_remove_med.apply(survivor)
            return f"{survivor.name} healed successfully with {medicine_type}"


    def sustain(self, survivor, sustenance_type):
        to_remove_supply = [s for s in self.supplies if s.__class__.__name__ == sustenance_type][-1]

        if survivor.needs_sustenance:
            self.supplies.remove(to_remove_supply)
            to_remove_supply.apply(survivor)
            return f"{survivor.name} sustained successfully with {sustenance_type}"


    def next_day(self):
        for s in self.survivors:
            s.needs -= s.age*2
        for survivor in self.survivors:
            self.sustain(survivor, "WaterSupply")
            self.sustain(survivor, "FoodSupply")

# from project.supply.food_supply import FoodSupply
# from project.supply.water_supply import WaterSupply
# bunker = Bunker()
# bunker.supplies = [WaterSupply()]
# print(bunker.food)






