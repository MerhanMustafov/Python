"""Upon initialization the class Storage will not receive any parameters.
 It should have 3 instance attributes:
    categories (empty list),
    topics (empty list),
    documents (empty list).
    The class should have the following methods:
"""
from project.category import Category
from project.topic import Topic
from project.document import Document
class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []
    """•	add_category(category:Category) – add the category if it is not in the list
        •	add_topic(topic:Topic) – add the topic if it does not exist
        •	add_document(document:Document) – add the document if it does not exist
    """
    def add_category(self, category: Category):
        if not category in self.categories:
            self.categories.append(category)

    def add_topic(self, topic:Topic):
        if not topic in self.topics:
            self.topics.append(topic)
    def add_document(self, document: Document):
        if not document in self.documents:
            self.documents.append(document)

    """•	edit_category(category_id: int, new_name:str) 
    – edit the name of the category with the provided id
        •	edit_topic(topic_id: int, new_topic: str, new_storage_folder: str) 
        – edit the topic with the given id
        •	edit_document(document_id: int, new_file_name: str) 
        – edit the document with the given id
    """

    def edit_category(self, category_id: int, new_name:str):
        for c in self.categories:
            if c.id == category_id:
                # c.edit(new_name)
                c.name = new_name
    
    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        for t in self.topics:
            if t.id == topic_id:
                # t.edit(new_topic, new_storage_folder)
                t.topic = new_topic
                t.storage_folder = new_storage_folder
    def edit_document(self, document_id: int, new_file_name: str):
        for d in self.documents:
            if d.id == document_id:
                # d.edit(new_file_name)
                d.file_name = new_file_name

    """•	delete_category(category_id) – delete the category with the provided id
        •	delete_topic(topic_id) – delete the topic with the provided id
        •	delete_document(document_id) – delete the document with the provided id
        •	get_document(document_id) – return the document with the provided id
        •	__repr__() – returns a string representation of each document on separate lines
    """
    def delete_category(self, category_id):
        for c in self.categories:
            if c.id == category_id:
                self.categories.remove(c)

    def delete_topic(self, topic_id):
        for t in self.topics:
            if t.id == topic_id:
                self.topics.remove(t)
    def delete_document(self, document_id):
        for d in self.documents:
            if d.id == document_id:
                self.documents.remove(d)

    def get_document(self, document_id):
        for d in self.documents:
            if d.id == document_id:
                return d

    def __repr__(self):
        message = []

        for d in self.documents:
            message.append(repr(d))
        
        return "\n".join(message)
