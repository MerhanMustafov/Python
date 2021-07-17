from project.common import gym_dataclass


Trainer = gym_dataclass({
    'name':str,
}, 'Trainer <{self.id}> {self.name}')


# class Trainer:
#     __counter = 1
#     def __init__(self, name:str):
#         self.name = name
#         self.id = __class__.__counter
#         __class__.__counter += 1
    
#     @staticmethod
#     def get_next_id():
#         return __class__.__counter

#     def __repr__(self):
#         return f"Trainer <{self.id}> {self.name}"