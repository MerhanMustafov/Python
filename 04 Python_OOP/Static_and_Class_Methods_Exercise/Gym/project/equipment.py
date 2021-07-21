from project.common import gym_dataclass


Equipment = gym_dataclass({
    'name': str,
}, 'Equipment <{self.id}> {self.name}'
)


# class Equipment:
#     id = 1
#     def __init__(self, name: str):
#         self.name= name
#         self.id = __class__.id
#         __class__.id += 1
#     def __repr__(self):
#         return f"Equipment <{self.id}> {self.name}"
#     @staticmethod  
#     def get_next_id():
#         return __class__.id 