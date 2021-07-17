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
        
        
