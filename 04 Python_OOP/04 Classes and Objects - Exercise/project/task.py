class Task:
    
    def __init__(self, name, due_date):
        self.name = name
        self.due_date = due_date
        self.comments = []
        self.completed = False

    def change_name(self, new_name: str):
        """ o	Change the name of the task and return the new name.
            o	If the new name is the same as the current name, return "Name cannot be the same."
"""
        if new_name == self.name:
            return "Name cannot be the same."
        self.name = new_name
        return new_name

    def change_due_date(self, new_date: str):
        ''' o	Change the due date of the task and return the new date.
            o	If the new date is the same as the current date, return "Date cannot be the same."
        ''' 
        if new_date == self.due_date:
            return "Date cannot be the same."
        self.due_date = new_date
        return new_date
    def add_comment(self, comment: str):
        self.comments.append(comment)
    
    def edit_comment(self, comment_number: int, new_comment: str):
        ''' o	The comment number value represents the index of the comment we want to edit.
         You should change the comment and return all the comments, separated by comma and space (", ")
            o	If the comment number is out of range, return "Cannot find comment."
''' 
        if 0 <= comment_number < len(self.comments):
            self.comments[comment_number] = new_comment
            return ", ".join(self.comments)  
        return "Cannot find comment."
    def details(self):
        return f"Name: {self.name} - Due Date: {self.due_date}"

