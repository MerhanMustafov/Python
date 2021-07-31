from project.task import Task


class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"

        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):

        for task in self.tasks:
             if task.name == task_name:
                task.completed = True
                return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"
    def clean_section(self):
        count_removed_tasks = 0
        for task in self.tasks:
            if task.completed:
                count_removed_tasks += 1
        self.tasks = [task for task in self.tasks if not task.completed]
        return f"Cleared {count_removed_tasks} tasks."
    def view_section(self):
        result = f"Section {self.name}:\n"
        for task in self.tasks:
            result += task.details() + "\n"
        return result[:-1]


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




# from typing import List
# from project.task import Task
#
#
# class Section:
#     tasks: List[Task] = []
#
#     def __init__(self, name: str) -> None:
#         self.name = name
#
#     def add_task(self, new_task: Task) -> str:
#         if new_task in Section.tasks:
#             return f'Task is already in the section {self.name}'
#
#         Section.tasks.append(new_task)
#         return f'Task {new_task.details()} is added to the section'
#
#     def complete_task(self, task_name: str) -> str:
#         for task in Section.tasks:
#             if task.name == task_name:
#                 task.completed = True
#                 return f'Completed task {task_name}'
#         return f'Could not find task with the name {task_name}'
#
#     def clean_section(self) -> str:
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
#
#     def view_section(self) -> str:
#         message = []
#         # nl = '\n'
#         message.append(f'Section {self.name}:')
#         for task in Section.tasks:
#             message.append(task.details())
#         return "\n".join(message)
#
#
#
# # task = Task("Make bed", "27/05/2020")
# # print(task.change_name("Go to University"))
# # print(task.change_due_date("28.05.2020"))
# # task.add_comment("Don't forget laptop")
# # print(task.edit_comment(0, "Don't forget laptop and notebook"))
# # print(task.details())
# # section = Section("Daily tasks")
# # print(section.add_task(task))
# # second_task = Task("Make bed", "27/05/2020")
# # section.add_task(second_task)
# # print(section.clean_section())
# # print(section.view_section())
