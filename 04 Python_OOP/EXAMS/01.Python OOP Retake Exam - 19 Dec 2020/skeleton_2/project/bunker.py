class Bunker:
    def __init__(self):
        self.survivors = []#Survivors obj
        self.supplies = []#Supplies OBJ
        self.medicine = []#Medicine OBJ

    @property
    def food(self):
        food_suppies = [el for el in self.supplies if el.__class__.__name__ == "FoodSupply"]
        if not food_suppies:
            raise IndexError("There are no food supplies left!")
        return food_suppies

    @property
    def water(self):
        water_supplies = [el for el in self.supplies if el.__class__.__name__ == "WaterSupply"]
        if not water_supplies:
            raise IndexError("There are no water supplies left!")
        return water_supplies

    @property
    def painkillers(self):
        painkillers_medicine = [el for el in self.medicine if el.__class__.__name__ == "Painkiller"]
        if not painkillers_medicine:
            raise IndexError("There are no painkillers left!")
        return painkillers_medicine

    @property
    def salves(self):
        salves_medicine = [el for el in self.medicine if el.__class__.__name__ == "Salve"]
        if not salves_medicine:
            raise IndexError("There are no salves left!")
        return salves_medicine

    def add_survivor(self, survivor):
        if survivor in self.survivors:
            raise ValueError(f"Survivor with name {survivor.name} already exists.")
        self.survivors.append(survivor)

    def add_supply(self, supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine):
        self.medicine.append(medicine)

    def heal(self, survivor, medicine_type: str):
        medicine = [m for m in self.medicine if m.__class__.__name__ == medicine_type][-1]
        if survivor.needs_healing:
            self.medicine.remove(medicine)
            medicine.apply(survivor)

            return f"{survivor.name} healed successfully with {medicine_type}"
    def sustain(self, survivor, sustenance_type: str):
        supply = [s for s in self.supplies if s.__class__.__name__ == sustenance_type][-1]
        if survivor.needs_sustenance:
            self.supplies.remove(supply)
            supply.apply(survivor)

            return f"{survivor.name} sustained successfully with {sustenance_type}"

    def next_day(self):
        for survivor in self.survivors:
            survivor.needs -= survivor.age * 2

        for survivor in self.survivors:
            food = "FoodSupply"
            water = "WaterSupply"
            self.sustain(survivor, food)
            self.sustain(survivor, water)