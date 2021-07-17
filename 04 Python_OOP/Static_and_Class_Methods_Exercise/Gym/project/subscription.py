from project.common import gym_dataclass


Subscription = gym_dataclass({
    'date': str,
    'customer_id': int,
    'trainer_id': int,
    'exercise_id': int,
}, 'Subscription <{self.id}> on {self.date}')

# class Subscription:
#     __counter = 1
#     def __init__(self, date:str, customer_id: int, trainer_id: int, exercise_id: int):
#         self.date = date
#         self.customer_id = customer_id
#         self.trainer_id = trainer_id
#         self.exercise_id = exercise_id
#         self.id = __class__.__counter
#         __class__.__counter += 1
    
#     @staticmethod
#     def get_next_id():
#         return __class__.__counter

#     def __repr__(self):
#         return f"Subscription <{self.id}> on {self.date}"