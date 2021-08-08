from project.hardware.hardware import Hardware
from project.software.software import Software

from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name:str, capacity:int, memory:int):
        power_hardware = PowerHardware(name, capacity, memory)
        System._hardware.append(power_hardware)

    @staticmethod
    def register_heavy_hardware(name:str, capacity:int, memory:int):
        heavy_hardware = HeavyHardware(name, capacity, memory)
        System._hardware.append(heavy_hardware)

    @staticmethod
    def register_express_software(hardware_name: str, name:str, capacity_consumption:int, memory_consumption:int):
        # try:
        #     hardware = [h for h in System._hardware if hardware_name == h.name][0]
        #
        #     express_software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        #     hardware.install(express_software)
        #     System._software.append(express_software)
        # except IndexError:
        #     return "Hardware does not exist"
        # except Exception as ex:
        #     return str(ex)

        for hardware in System._hardware:
            if hardware_name == hardware.name:
                express_software = ExpressSoftware(name, capacity_consumption, memory_consumption)
                try:
                    hardware.install(express_software)
                    System._software.append(express_software)
                    return
                except Exception as ex:
                    return str(ex)
        return "Hardware does not exist"

    @staticmethod
    def register_light_software(hardware_name: str, name:str, capacity_consumption:int, memory_consumption:int):
        # try:
        #     hardware = [h for h in System._hardware if hardware_name == h.name][0]
        #
        #     light_software = LightSoftware(name, capacity_consumption, memory_consumption)
        #     hardware.install(light_software)
        #     System._software.append(light_software)
        #
        # except IndexError:
        #     return "Hardware does not exist"
        # except Exception as ex:
        #     return str(ex)
        for hardware in System._hardware:
            if hardware_name == hardware.name:
                light_software = LightSoftware(name, capacity_consumption, memory_consumption)
                try:
                    hardware.install(light_software)
                    System._software.append(light_software)
                    return
                except Exception as ex:
                    return str(ex)
        return "Hardware does not exist"

    @staticmethod
    def release_software_component(hardware_name:str, software_name:str):
        try:
            hard_name = [hardware for hardware in System._hardware if hardware_name == hardware.name][0]
            soft_name = [software for software in System._software if software_name == software.name][0]
            hard_name.uninstall(soft_name)
            System._software.remove(soft_name)

        except IndexError:
            return "Some of the components do not exist"


    @staticmethod
    def analyze():
        # total_used_memory = sum([h.used_memory for h in System._hardware])
        # total_memory = sum([h.memory for h in System._hardware])
        # total_used_space = sum([h.used_capacity for h in System._hardware])
        # total_capacity = sum([h.capacity for h in System._hardware])
        #
        # return f"System Analysis\n" \
        #        f"Hardware Components: {len(System._hardware)}\n" \
        #        f"Software Components: {len(System._software)}\n" \
        #        f"Total Operational Memory: {total_used_memory} / {total_memory}\n" \
        #        f"Total Capacity Taken: {total_used_space} / {total_capacity}"
        massage = []
        new_line = "\n"
        massage.append("System Analysis")
        massage.append(f"Hardware Components: {len(System._hardware)}")
        massage.append(f"Software Components: {len(System._software)}")
        total_used_mem = sum([s.memory_consumption for s in System._software])
        total_mem = sum([h.memory for h in System._hardware])
        massage.append(f"Total Operational Memory: {total_used_mem} / {total_mem}")
        total_used_space = sum([s.capacity_consumption for s in System._software])
        total_cap = sum([h.capacity for h in System._hardware])
        massage.append(f"Total Capacity Taken: {total_used_space} / {total_cap}")
        result = new_line.join(massage)
        return result


    @staticmethod
    def system_split():

        # result = ""
        # for h in System._hardware:
        #     express_software_components = [s for s in h.software_components if
        #                                    s.__class__.__name__ == "ExpressSoftware"]
        #     light_software_components = [s for s in h.software_components
        #                                  if s.__class__.__name__ == "LightSoftware"]
        #     names = ', '.join([s.name for s in h.software_components])
        #
        #     result += f"Hardware Component - {h.name}\n"
        #     result += f"Express Software Components: {len(express_software_components)}\n"
        #     result += f"Light Software Components: {len(light_software_components)}\n"
        #     result += f"Memory Usage: {sum([s.memory_consumption for s in h.software_components])} / {h.memory}\n"
        #     result += f"Capacity Usage: {sum([s.capacity_consumption for s in h.software_components])} / {h.capacity}\n"
        #     result += f"Type: {h.type}\n"
        #     result += f"Software Components: {names if names else None}"
        # return result
        result = ""
        new_line = "\n"
        for h in System._hardware:
            result += (f"Hardware Component - {h.name}") + new_line
            express_soft = [express for express in h.software_components if express.__class__.__name__ == "ExpressSoftware"]
            light_soft = [light for light in h.software_components if light.__class__.__name__ == "LightSoftware"]
            result +=  (f"Express Software Components: {len(express_soft)}")+ new_line
            result += (f"Light Software Components: {len(light_soft)}")+ new_line
            total_mem_used = sum([x.memory_consumption for x in h.software_components])
            total_har_mem = h.memory
            result += (f"Memory Usage: {total_mem_used} / {total_har_mem}")+ new_line
            total_cap_used = sum([x.capacity_consumption for x in h.software_components])
            total_cap_mem = h.capacity
            result += (f"Capacity Usage: {total_cap_used} / {total_cap_mem}")+ new_line
            result += (f"Type: {h.type}")+ new_line
            names = ', '.join([s.name for s in h.software_components])
            result += (f"Software Components: {names if names else None}")

        return result







