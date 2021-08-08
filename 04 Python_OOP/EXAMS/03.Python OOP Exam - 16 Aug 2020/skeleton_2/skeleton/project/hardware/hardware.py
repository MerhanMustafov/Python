from project.software.software import Software


class Hardware:
    def __init__(self, name:str, type:str, capacity:int, memory:int):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    def install(self, software:Software):
        used_memory = sum([s.memory_consumption for s in self.software_components]) + software.memory_consumption
        used_capacity = sum([s.capacity_consumption for s in self.software_components]) + software.capacity_consumption
        if not (self.capacity >= used_capacity and
            self.memory >= used_memory):
            raise Exception("Software cannot be installed")

        self.software_components.append(software)



    def uninstall(self, software:Software):
        # if software in self.software_components:
        self.software_components.remove(software)

