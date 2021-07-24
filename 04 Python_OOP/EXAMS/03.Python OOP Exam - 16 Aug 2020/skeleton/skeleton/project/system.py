from project.hardware.hardware import Hardware
from project.software.software import Software
from project.hardware.power_hardware import PowerHardware
from project.hardware.heavy_hardware import HeavyHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware
from typing import List


class System:
    _hardware: List[Hardware] = []
    _software: List[Software] = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        """Create a PowerHardware instance and add it to the hardware list"""
        power_hardware = PowerHardware(name, capacity, memory)
        # if power_hardware not in System._hardware:
        System._hardware.append(power_hardware)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        """Create a HeavyHardware instance and add it to the hardware list"""
        heavy_hardware = HeavyHardware(name, capacity, memory)
        # if heavy_hardware not in System._hardware:
        System._hardware.append(heavy_hardware)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        """•	If the hardware with the given name does NOT exist,
                 return a message "Hardware does not exist"
            •	Otherwise, create an ExpressSoftware instance, install it on the hardware
                 (if possible) and add it to the software list (if installed successfully)
            •	If the installation is not possible return the message of the raised Exception
        """
        try:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
            software = ExpressSoftware(name, capacity_consumption, memory_consumption)
            hardware.install(software)
            System._software.append(software)
        except IndexError:
            return "Hardware does not exist"
        except Exception as ex:
            return str(ex)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        """•	If the hardware with the given name does NOT exist,
                return a message "Hardware does not exist"
            •	Otherwise, create a LightSoftware instance, install it on the hardware
                (if possible) and add it to the software list (if installed successfully)
            •	If the installation is not possible return the message of the raised Exception
        """
        try:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
            software = LightSoftware(name, capacity_consumption, memory_consumption)
            hardware.install(software)
            System._software.append(software)
        except IndexError:
            return "Hardware does not exist"
        except Exception as ex:
            return str(ex)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        """•	If both components exist on the system, uninstall the software from the given hardware
            •	Otherwise, return a message "Some of the components do not exist"
        """
        try:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
            software = [s for s in System._software if s.name == software_name][0]
            hardware.uninstall(software)
            System._software.remove(software)
        except IndexError:
            return "Some of the components do not exist"

    @staticmethod
    def analyze():
        total_used_memory = sum([h.used_memory for h in System._hardware])
        total_memory = sum([h.memory for h in System._hardware])
        total_used_space = sum([h.used_capacity for h in System._hardware])
        total_capacity = sum([h.capacity for h in System._hardware])

        return f"System Analysis\n"\
            f"Hardware Components: {len(System._hardware)}\n" \
            f"Software Components: {len(System._software)}\n" \
            f"Total Operational Memory: {total_used_memory} / {total_memory}\n" \
            f"Total Capacity Taken: {total_used_space} / {total_capacity}"

    @staticmethod
    def system_split():
        result = ""
        for h in System._hardware:
            express_software_components = [s for s in h.software_components if
                                           s.__class__.__name__ == "ExpressSoftware"]
            light_software_components = [s for s in h.software_components
                                         if s.__class__.__name__ == "LightSoftware"]
            names = ', '.join([s.name for s in h.software_components])

            result += f"Hardware Component - {h.name}\n"
            result += f"Express Software Components: {len(express_software_components)}\n"
            result += f"Light Software Components: {len(light_software_components)}\n"
            result += f"Memory Usage: {sum([s.memory_consumption for s in h.software_components])} / {h.memory}\n"
            result += f"Capacity Usage: {sum([s.capacity_consumption for s in h.software_components])} / {h.capacity}\n"
            result += f"Type: {h.type}\n"
            result += f"Software Components: {names if names else None}"
        return result
