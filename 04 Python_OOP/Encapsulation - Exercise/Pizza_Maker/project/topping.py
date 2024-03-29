
class Topping:
    def __init__(self, topping_type: str, weight: float):
        self.topping_type = topping_type
        self.weight = weight

    @property
    def topping_type(self):
        return self.__topping_type

    @topping_type.setter
    def topping_type(self, value):
        if value == "":
            raise ValueError("The topping type cannot be an empty string")
        self.__topping_type = value

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        if value <= 0:
            raise ValueError("The weight cannot be less or equal to zero")
        self.__weight = value
























# class Topping:
#     def __init__(self, topping_type: str, weight: int):
#         self.topping_type = topping_type
#         self.weight = weight
#
#     @property
#     def topping_type(self):
#         return self.__topping_type
#     @topping_type.setter
#     def topping_type(self, topping):
#         if topping == "":
#             raise ValueError("The topping type cannot be an empty string")
#         self.__topping_type = topping
#
#     @property
#     def weight(self):
#         return self.__weight
#     @weight.setter
#     def weight(self, w):
#         if w <= 0:
#             raise ValueError("The weight cannot be less or equal to zero")
#         self.__weight = w