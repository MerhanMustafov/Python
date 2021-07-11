# from typing import List
# class Book:
#     def __init__(self, name, author, pages = []):
#         self.name = name
#         self.author = author
#         self.pages: List[]
#     # def add_pages(self):
#     #     for x in range(5):
#     #         self.pages.append(1)
#     #         print(self.pages)

# book = Book("Rainbow", "Merho", 230)
# # book.add_pages()
# print(book.pages)
# # lst = [1, 2, 3, 4, 5]
# # lst.append(55555555)
# # print(lst)

# class Example:
#     def print_txt():
#         return "Merho"

# p = Example
# print(p.print_txt())


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
# class Employee(Person):
#     def __init__(self, name, data, age=None):
#         super().__init__(name, age)
#         self.data = data
#     def __str__(self):
#         return f"Person {self.name} age {self.age}"
# p = Employee("Pesho", 28)
# print(p)

class BankAccount:
    def __init__(self, name):
        self.name = name
        self._number = 6546546545
        self.cvv = 689
        self.expiration_date = "24.16.2020"
    def __repr__(self):
        return f"Name: {self.name}\nCardNumber: \nCVV: {self.cvv}\nExpirationDate: {self.expiration_date}"
class Inherit(BankAccount):
    def __init__(self, name, percent):
        super().__init__(name)
        print(self._number)
        self.percent = percent
person_account = Inherit("Merhan", 20)
print(person_account._number)

# print(person_account.number)