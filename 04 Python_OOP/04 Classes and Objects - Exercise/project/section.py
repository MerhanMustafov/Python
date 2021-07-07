from project.task import Task
class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []
    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        # d = self.project.task.details(self)
        return f"Task {self.Task.details(self)} is added to the section"