from typing import List
from three import Three
def unpacking(skills):
    return [str(x) for x in skills]
class One(Three):
    def __init__(self, name, age, skills):
        super().__init__(name, age)
        self.skills: List[skills] = []

    def upgrade_skills(self):
        if self.age > 5:
            for x in range(self.age-5):
                self.skills.append(self.age+x)
    def get_info(self):
        return f"Person {self.name} {self.age} has these skills {' '.join(unpacking(self.skills))}"
    
