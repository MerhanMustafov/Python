class Bunker:
    def __init__(self):
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
        pass
    def add_supply(self, supply):#obj
        pass
    def add_medicine(self, medicine):#obj
        pass
    def heal(self, survivor, medicine_type):
        pass
    def sustain(survivor, sustenance_type):
        pass
    def next_day(self):
        pass




