class Customer:
    def __init__(self, name: str, age: int, id: int):
        self.name = str(name)
        self.age = int(age)
        self.id = int(id)
        self.rented_dvds = list()

    def __repr__(self):
        dvds = ", ".join([d.name for d in self.rented_dvds])
        return f"{self.id}: {self.name} of age {self.age} has {len(self.rented_dvds)} rented DVD's ({dvds})"