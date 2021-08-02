from project.dvd import DVD
class Customer:
    def __init__(self,name: str, age: int, id: int):
        self.name = name
        self.age = age
        self.id = id
        self.rented_dvds = []
    def add_dvd_to_rented(self, dvd):
        self.rented_dvds.append(dvd)

    def __repr__(self):
        return f"{self.id}: {self.name}" \
               f" of age {self.age}" \
               f" has {len(self.rented_dvds)}" \
               f" rented DVD's ({', '.join([d.name for d in self.rented_dvds])})"
#     {dvd_names joined by comma and space}



































# class Customer:
#     def __init__(self, name: str, age: int, id: int):
#         self.name = str(name)
#         self.age = int(age)
#         self.id = int(id)
#         self.rented_dvds = list()
#
#     def __repr__(self):
#         dvds = ", ".join([d.name for d in self.rented_dvds])
#         return f"{self.id}: {self.name} of age {self.age} has {len(self.rented_dvds)} rented DVD's ({dvds})"