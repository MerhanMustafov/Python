from typing import List
from project.customer import Customer
from project.dvd import DVD



C_DVD_CAPACITY = 15
C_CUSTOMER_CAPACITY = 10

class MovieWorld:
    DVD_CAPACITY = C_DVD_CAPACITY
    CUSTOMER_CAPACITY = C_CUSTOMER_CAPACITY

    def __init__(self, name: str):
        self.name = str(name)
        self.customers = list()
        self.dvds = list()
    @staticmethod
    def dvd_capacity() -> int:
        return __class__.DVD_CAPACITY
    @staticmethod
    def customer_capacity() -> int:
        return __class__.CUSTOMER_CAPACITY

    def add_customer(self, c: Customer) -> bool:

        if len(self.customers) < self.customer_capacity():
            self.customers.append(c)
            return True
        return False

    def add_dvd(self, d) -> bool:
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(d)
            return True
        return False

    def rent_dvd(self, customer_id: int, dvd_id: int) -> str:
        # dvd: DVD = [d for d in self.dvds if d.id == dvd_id][0]
        dvd: DVD = list(filter(lambda d: d.id == dvd_id, self.dvds))[0]
        customer: Customer = list(filter(lambda _: _.id == customer_id, self.customers))[0]
        if dvd_id in [d.id for d in customer.rented_dvds]:
            return f"{customer.name} has already rented {dvd.name}"
        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
        if dvd.is_rented:
            return "DVD is already rented"
        dvd.is_rented = True
        customer.rented_dvds.append(dvd)
        return f"{customer.name} has successfully rented {dvd.name}"


    def return_dvd(self, customer_id, dvd_id):
        customer: Customer =  list(filter(lambda _: _.id == customer_id, self.customers))[0]
        if dvd_id in [d.id for d in customer.rented_dvds]:
            dvd = list(filter(lambda d: d.id == dvd_id, self.dvds))[0]
            dvd.is_rented = False
            customer.rented_dvds.remove(dvd)
            return f"{customer.name} has successfully returned {dvd.name}"
        return f"{customer.name} does not have that DVD"
    def __repr__(self) -> str:
        result = ""
        customers = "\n".join([c.__repr__() for c in self.customers])
        dvds = "\n".join([d.__repr__() for d in self.dvds])
        result += f"{customers}\n"
        result += dvds
        return result





# from project.customer import Customer
# class MovieWorld:
#     def __init__(self, name):
#         self.name = name
#         self.customers = []
#         self.dvds = []
#
#     def dvd_camacity(self):
#         return 15
#     def customer_capacity(self):
#         return 10
#
#     def add_customer(self, customer):
#         if len(self.customers) <= self.customer_capacity():
#             if customer not in self.customers:
#                 self.customers.append(customer)
#
#     def add_dvd(self, DVD):
#         if len(self.dvds) <= self.dvd_camacity():
#             if DVD not in self.dvds:
#                 self.dvds.append(DVD)
#
#     def rent_dvd(self, customer_id: int, dvd_id: int):
#
#
#         dvd = [d for d in self.dvds if dvd_id == d.id][0]
#         customer = [c for c in self.customers if customer_id == c.id][0]
#
#         if dvd_id in [d.id for d in customer.rented_dvds]:
#             return f"{customer.name} has already rented {dvd.name}"
#
#         if dvd.is_rented:
#             return f"DVD is already rented"
#
#         # can't rent because of age restriction
#         if customer.age < dvd.age_restriction:
#             return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
#
#         # rented
#         Customer.add_dvd_to_rented(customer, dvd)
#         dvd.is_rented = True
#         return f"{customer.name} has successfully rented {dvd.name}"
#
#
#     def return_dvd(self, customer_id, dvd_id):
#
#         customer = [c for c in self.customers if customer_id == c.id][0]
#         if dvd_id in [d.id for d in customer.rented_dvds][0]:
#             dvd = [d for d in self.dvds if dvd_id == d.id][0]
#
#             dvd.is_rented = False
#             customer.rented_dvds.remove(dvd)
#             return f"{customer.name} has successfully returned {dvd.name}"
#         return f"{customer.name} does not have that DVD"
#
#
#     def __repr__(self):
#         result = ""
#         for customer in self.customers:
#             result += customer.__repr__() + "\n"
#         for dvd in self.dvds:
#             result += dvd.__repr__() + "\n"
#         return result[:-1]


# from project.customer import Customer
# from project.dvd import DVD
#
#
# c1 = Customer("John", 16, 1)
# c2 = Customer("Anna", 55, 2)
#
# d1 = DVD("Black Widow", 1, 2020, "April", 18)
# d2 = DVD.from_date(2, "The Croods 2", "23.12.2020", 3)
#
# movie_world = MovieWorld("The Best Movie Shop")
#
# movie_world.add_customer(c1)
# movie_world.add_customer(c2)
#
# movie_world.add_dvd(d1)
# movie_world.add_dvd(d2)
#
# print(movie_world.rent_dvd(1, 1))
# print(movie_world.rent_dvd(2, 1))
# print(movie_world.rent_dvd(1, 2))
#
# print(movie_world)



































