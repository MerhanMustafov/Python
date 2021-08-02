class Customer:
    autoincremented = 1
    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email
        self.id = Customer.autoincremented
        Customer.autoincremented += 1




    @staticmethod
    def get_next_id():
        return Customer.autoincremented

    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"


# customer = Customer("John", "adress", "mail@mail.bg")
# print(customer.id)
# print(Customer.autoincremented)
# print(customer.name)
# print(customer)
# print(customer.autoincremented)



























#
# class Customer:
#     #autoincremented starting from 1
#     id = 1
#     def __init__(self, name: str, address: str, email: str):
#         self.name = name
#         self.address = address
#         self.email = email
#         self.id = __class__.id
#         __class__.id += 1
#
#
#     def __repr__(self):
#         return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"
#
#     @staticmethod
#     def get_next_id():
#         return __class__.id