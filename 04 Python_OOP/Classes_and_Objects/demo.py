# class Smartphone:
#     def __init__(self, memory):
#         self.memory = memory
#         self.apps = []
#         self.is_on = False
#
#     def power(self):
#         if not self.is_on:
#             self.is_on = True
#         else:
#             self.is_on = False
#
#     def install(self, app, app_memory):
#         if self.memory >= app_memory and self.is_on:
#             self.apps.append(app)
#             self.memory -= app_memory
#             return f"Installing {app}"
#         elif self.memory >= app_memory and not self.is_on:
#             return f"Turn on your phone to install {app}"
#         return f"Not enough memory to install {app}"
#
#     def status(self):
#         return f"Total apps: {len(self.apps)}. Memory left: {self.memory}"
#
#     # def is_enough_memory_space(self, memory, app_memory):
#     #     return memory >= app_memory
#
# smartphone = Smartphone(100)
# print(smartphone.install("Facebook", 60))
# smartphone.power()
# print(smartphone.install("Facebook", 60))
# print(smartphone.install("Messenger", 20))
# print(smartphone.install("Instagram", 40))
# print(smartphone.status())
#
#
#





# class Glass:
#     capacity = 250
#     def __init__(self):
#         self.content = 0
#     def fill(self, ml):
#         if ml + self.content <= self.capacity:
#             self.content += ml
#             return f"Glass filled with {ml} ml"
#         return f"Cannot add {ml} ml"
#     def empty(self):
#         self.content = 0
#         return "Glass is now empty"
#     def info(self):
#         space_left = self.capacity - self.content
#         return f"{space_left} ml left"
#
# glass = Glass()
# print(glass.fill(100))
# print(glass.fill(200))
# print(glass.empty())
# print(glass.fill(200))
# print(glass.info())


# class Circle:
#     pi = 3.14
#     def __init__(self, radius):
#         self.radius = radius
#
#     def set_radius(self, new_radius):
#         self.radius = new_radius
#     def get_area(self):
#         area = self.pi * self.radius**2
#         return area
#     def get_circumference(self):
#         circumference = 2 * self.pi * self.radius
#         return circumference
# circle = Circle(10)
# circle.set_radius(12)
# print(circle.get_area())
# print(circle.get_circumference())






# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def set_x(self, new_x):
#         self.x = new_x
#     def set_y(self, new_y):
#         self.y = new_y
#     def __str__(self):
#         return f"The point has coordinates ({self.x},{self.y})"
#
#
# p = Point(2, 4)
# print(p)
# p.set_x(3)
# p.set_y(5)
# print(p)
#
#


# class Vehicle:
#     def __init__(self, mileage, max_speed = 150):
#         self.mileage = mileage
#         self.max_speed = max_speed
#         self.gadgets = []
#
# car = Vehicle(20)
# print(car.max_speed)
# print(car.mileage)
# print(car.gadgets)
# car.gadgets.append('Hudly Wireless')
# print(car.gadgets)
