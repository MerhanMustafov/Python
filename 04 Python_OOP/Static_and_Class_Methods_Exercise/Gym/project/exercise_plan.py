class ExercisePlan:
    autoincremented = 1
    def __init__(self, trainer_id: int, equipment_id: int, duration: int):
        self.trainer_id = trainer_id
        self.equipment_id = equipment_id
        self.duration = duration
        self.id = ExercisePlan.autoincremented
        ExercisePlan.autoincremented += 1

    @classmethod
    def from_hours(cls,trainer_id:int, equipment_id:int, hours:int):
        hours = hours*60
        return cls(trainer_id, equipment_id, hours)

    @staticmethod
    def get_next_id():
        return ExercisePlan.autoincremented

    def __repr__(self):
        return f"Plan <{self.id}> with duration {self.duration} minutes"






















# from project.common import gym_dataclass
#
#
# @classmethod
# def from_hours(cls, trainer_id: int, equipment_id: int, hours: int):
#     return cls(trainer_id, equipment_id, hours*60)
#
#
# ExercisePlan = gym_dataclass({
#     'trainer_id': int,
#     'equipment_id': int,
#     'duration': int,
# }, 'Plan <{self.id}> with duration {self.duration} minutes'
# )
#
# ExercisePlan.from_hours = from_hours
#
#
# # class ExercisePlan:
# #     __counter = 1
# #     def __init__(self, trainer_id: int, equipment_id: int, duration: int ):
# #         self.trainer_id = trainer_id
# #         self.equipment_id = equipment_id
# #         self.duration = duration
# #         self.id = __class__.__counter
# #         __class__.__counter += 1
#
# #     @staticmethod
# #     def get_next_id():
# #         return __class__.__counter
#
# #     @classmethod
# #     def from_hours(cls ,trainer_id:int, equipment_id:int, hours:int):
# #         return cls(trainer_id, int(equipment_id), int(hours) * 60)
#
# #     def __repr__(self):
# #         return f"Plan <{self.id}> with duration {self.duration} minutes"
#
#
#
