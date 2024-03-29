class Player:
    def __init__(self, name:str, sprint:int, dribble:int, passing:int, shooting:int):
        self.__name = name
        self.__sprint = sprint
        self.__dribble = dribble
        self.__passing = passing
        self.__shooting = shooting

    @property
    def name(self):
        return self.__name

    def __str__(self):
        return f"Player: {self.__name}\n"\
                f"Sprint: {self.__sprint}\n"\
                f"Dribble: {self.__dribble}\n"\
                f"Passing: {self.__passing}\n"\
                f"Shooting: {self.__shooting}"





















# """Create a class called Player. Upon initialization it should receive:
# •	Private attribute name: string
# •	Private attribute sprint: int
# •	Private attribute dribble: int
# •	Private attribute passing: int
# •	Private attribute shooting: int
# """
#
# class Player:
#     def __init__(self, name: str, sprint: int, dribble: int, passing: int, shooting: int):
#         self.__name = name
#         self.__sprint = sprint
#         self.__dribble = dribble
#         self.__passing = passing
#         self.__shooting = shooting
#     """"Player: {name}
#         Sprint: {sprint}
#         Dribble: {dribble}
#         Passing: {passing}
#         Shooting: {shooting}"
#
# """
#     @property
#     def name(self):
#         return self.__name
#
#     def __str__(self):
#         return f"Player: {self.__name}\n" \
#                 f"Sprint: {self.__sprint}\n" \
#                 f"Dribble: {self.__dribble}\n" \
#                 f"Passing: {self.__passing}\n" \
#                 f"Shooting: {self.__shooting}"