from project.software.software import Software
from typing import List


class Hardware:
    def __init__(self, name: str, type: str, capacity: int, memory: int):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.memory = memory
        self.software_components: List[Software] = [] 

    def install(self, software: Software):
        """If there is enough capacity and memory,
        add the software object to the software_components.
        Otherwise, raise Exception with message "Software cannot be installed"""
        if not (software.capacity_consumption <= self.available_capacity and software.memory_consumption <= self.available_memory):
            raise Exception("Software cannot be installed")    
        self.software_components.append(software)

    def uninstall(self, software: Software):
        # if software in self.software_components:
        self.software_components.remove(software)

    @property
    def available_memory(self):
        return self.memory - self.used_memory

    @property
    def available_capacity(self):
        return self.capacity - self.used_capacity

    @property
    def used_capacity(self):
        return sum([s.capacity_consumption for s in self.software_components])

    @property
    def used_memory(self):
        return sum([s.memory_consumption for s in self.software_components])
