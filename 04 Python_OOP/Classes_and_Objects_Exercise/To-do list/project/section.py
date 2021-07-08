from typing import List
from project.task import Task


class Section:
    tasks: List[Task] = []

    def __init__(self, name: str) -> None:
        self.name = name

    def add_task(self, new_task: Task) -> str:
        if new_task in Section.tasks:
            return f'Task is already in the section {self.name}'

        Section.tasks.append(new_task)
        return f'Task {new_task.details()} is added to the section'

    def complete_task(self, task_name: str) -> str:
        for task in Section.tasks:
            if task.name == task_name:
                task.completed = True
                return f'Completed task {task_name}'
        return f'Could not find task with the name {task_name}'

    def clean_section(self) -> str:
        cleared_tasks = 0
        i = 0
        end = len(Section.tasks)
        while i < end:
            task = Section.tasks[i]
            if task.completed:
                Section.tasks.pop(i)
                cleared_tasks += 1
            i += 1
        return f'Cleared {cleared_tasks} tasks.'

    def view_section(self) -> str:
        message = []
        nl = '\n'
        message.append(f'Section {self.name}:')
        for task in Section.tasks:
            message.append(task.details())
        return nl.join(message)

# from task import Task

# class Section:
#     tasks = []
#     def __init__(self, name: str):
#         self.name = name
        
#     def add_task(self, new_task: Task):
#         if new_task in Section.tasks:
#             return f"Task is already in the section {self.name}"
#         Section.tasks.append(new_task)
#         return f"Task {new_task.details()} is added to the section"
#     def complete_task(task_name: str):
#         for task in Section.tasks:
#             if task.name == task_name:
#                 task.completed = True
#                 return f'Completed task {task_name}'
#         return f'Could not find task with the name {task_name}'
    
#     def clean_section(self):
#         cleared_tasks = 0
#         i = 0
#         end = len(Section.tasks)
#         while i < end:
#             task = Section.tasks[i]
#             if task.completed:
#                 Section.tasks.pop(i)
#                 cleared_tasks += 1
#             i += 1
#         return f'Cleared {cleared_tasks} tasks.'


#     def view_section(self):
#         message = []
#         nl = '\n'
#         message.append(f'Section {self.name}:')
#         for task in Section.tasks:
#             message.append(task.details())
#         return nl.join(message)

task = Task("Make bed", "27/05/2020")
print(task.change_name("Go to University"))
print(task.change_due_date("28.05.2020"))
task.add_comment("Don't forget laptop")
print(task.edit_comment(0, "Don't forget laptop and notebook"))
print(task.details())
section = Section("Daily tasks")
print(section.add_task(task))
second_task = Task("Make bed", "27/05/2020")
section.add_task(second_task)
print(section.clean_section())
print(section.view_section())
