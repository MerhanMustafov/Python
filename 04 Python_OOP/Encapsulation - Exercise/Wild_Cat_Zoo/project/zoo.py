# from project.worker import Worker
# from project.animal import Animal
class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget >= price and\
            self.__animal_capacity > len(self.animals):
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        if self.__animal_capacity > len(self.animals) and\
            self.__budget < price:
            return "Not enough budget"
        return "Not enough space for animal"


    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        try:
            worker = [w for w in self.workers if w.name == worker_name][0]
            self.workers.remove(worker)
            return f"{worker_name} fired successfully"
        except IndexError:
            return f"There is no {worker_name} in the zoo"

        # for worker in self.workers:
        #     if worker_name == worker.name:
        #         self.workers.remove(worker)
        #         return f"{worker_name} fired successfully"
        # return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_money_neede_for_workers = sum([w.salary for w in self.workers])
        if self.__budget >= total_money_neede_for_workers:
            self.__budget -= total_money_neede_for_workers
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_money_for_care = sum([m_f_c.money_for_care for m_f_c in self.animals])
        if self.__budget >= total_money_for_care:
            self.__budget -= total_money_for_care
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return f"You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = [l for l in self.animals if l.__class__.__name__ == "Lion"]
        tigers = [t for t in self.animals if t.__class__.__name__ == "Tiger"]
        cheetahs = [ch for ch in self.animals if ch.__class__.__name__ == "Cheetah"]
        result = f"You have {len(self.animals)} animals\n"
        result += f"-"*5 + " " +f"{len(lions)} Lions:\n"
        result += "\n".join([l.__repr__() for l in lions])

        result += "\n" + f"-" * 5 + " " + f"{len(tigers)} Tigers:\n"
        result += "\n".join([t.__repr__() for t in tigers])

        result += "\n" +f"-" * 5 + " " + f"{len(cheetahs)} Cheetahs:\n"
        result += "\n".join([ch.__repr__() for ch in cheetahs])


        return result
        # result = f"You have {len(self.animals)} animals\n"
        # lions_count = len([animal for animal in self.animals if animal.__class__.__name__ == "Lion"])
        # result += f"-"*5 + " " +f"{lions_count} Lions:\n"
        # for animal in self.animals:
        #     if animal.__class__.__name__ == "Lion":
        #         result += animal.__repr__() + "\n"
        # tiger_count = len([animal for animal in self.animals if animal.__class__.__name__ == "Tiger"])
        # result += f"-" * 5 + " "  + f"{tiger_count} Tigers:\n"
        # for animal in self.animals:
        #     if animal.__class__.__name__ == "Tiger":
        #         result += animal.__repr__() + "\n"
        # cheetah_count = len([animal for animal in self.animals if animal.__class__.__name__ == "Cheetah"])
        # result += f"-" * 5 + " " + f"{cheetah_count} Cheetahs:\n"
        # for animal in self.animals:
        #     if animal.__class__.__name__ == "Cheetah":
        #         result += animal.__repr__() + "\n"
        # return result[:-1]

    def workers_status(self):
        keepers = [k for k in self.workers if k.__class__.__name__ == "Keeper"]
        caretakers = [c for c in self.workers if c.__class__.__name__ == "Caretaker"]
        vets = [v for v in self.workers if v.__class__.__name__ == "Vet"]
        result = f"You have {len(self.workers)} workers\n"
        result += f"-" * 5 + " " + f"{len(keepers)} Keepers:\n"
        result += ", ".join([k.__repr__() for k in keepers])

        result += "\n" + f"-" * 5 + " " + f"{len(caretakers)} Caretakers:\n"
        result += ", ".join([c.__repr__() for c in caretakers])

        result += "\n" + f"-" * 5 + " " + f"{len(vets)} Vets:\n"
        result += ", ".join([v.__repr__() for v in vets])

        return result
        # result = f"You have {len(self.workers)} workers\n"
        # keeper_count = len([worker for worker in self.workers if worker.__class__.__name__ == "Keeper"])
        # result += f"-" * 5 + " " + f"{keeper_count} Keepers:\n"
        # for worker in self.workers:
        #     if worker.__class__.__name__ == "Keeper":
        #         result += worker.__repr__() + "\n"
        # caretakers_count = len([worker for worker in self.workers if worker.__class__.__name__ == "Caretaker"])
        # result += f"-" * 5 + " "  + f"{caretakers_count} Caretakers:\n"
        # for worker in self.workers:
        #     if worker.__class__.__name__ == "Caretaker":
        #         result += worker.__repr__() + "\n"
        # vets_count = len([worker for worker in self.workers if worker.__class__.__name__ == "Vet"])
        # result += f"-" * 5 + " " + f"{vets_count} Vets:\n"
        # for worker in self.workers:
        #     if worker.__class__.__name__ == "Vet":
        #         result += worker.__repr__() + "\n"
        # return result[:-1]


# from project.worker import Worker
# from project.animal import Animal
# from project.lion import Lion
# from project.tiger import Tiger
# from project.cheetah import Cheetah
# from project.keeper import Keeper
# from project.vet import Vet
# from project.caretaker import Caretaker
# from project.zoo import Zoo
#
# import unittest
#
#
# class Tests(unittest.TestCase):
#     def test_lion_init(self):
#         l = Lion("a", "m", 4)
#         self.assertEqual(l.name, "a")
#         self.assertEqual(l.gender, "m")
#         self.assertEqual(l.age, 4)
#
#     def test_lion_get_needs(self):
#         l = Lion("b", "f", 2)
#         res = l.money_for_care
#         self.assertEqual(res, 50)
#
#     def test_lion_repr(self):
#         l = Lion("b", "f", 2)
#         res = str(l)
#         self.assertEqual(res, "Name: b, Age: 2, Gender: f")
#
#     def test_tiger_init(self):
#         t = Tiger("z", "m", 1)
#         self.assertEqual(t.name, "z")
#         self.assertEqual(t.gender, "m")
#         self.assertEqual(t.age, 1)
#
#     def test_tiger_get_needs(self):
#         t = Tiger("v", "f", 7)
#         res = t.money_for_care
#         self.assertEqual(res, 45)
#
#     def test_tiger_repr(self):
#         t = Tiger("w", "f", 3)
#         res = str(t)
#         self.assertEqual(res, "Name: w, Age: 3, Gender: f")
#
#     def test_cheetah_init(self):
#         c = Cheetah("l", "f", 3)
#         self.assertEqual(c.name, "l")
#         self.assertEqual(c.gender, "f")
#         self.assertEqual(c.age, 3)
#
#     def test_cheetah_get_needs(self):
#         c = Cheetah("r", "m", 6)
#         res = c.money_for_care
#         self.assertEqual(res, 60)
#
#     def test_cheetah_repr(self):
#         c = Cheetah("n", "f", 2)
#         res = str(c)
#         self.assertEqual(res, "Name: n, Age: 2, Gender: f")
#
#     def test_keeper_init(self):
#         k = Keeper("john", 21, 200)
#         self.assertEqual(k.name, "john")
#         self.assertEqual(k.age, 21)
#         self.assertEqual(k.salary, 200)
#
#     def test_keeper_repr(self):
#         k = Keeper("ally", 36, 190)
#         res = str(k)
#         self.assertEqual(res, "Name: ally, Age: 36, Salary: 190")
#
#     def test_vet_init(self):
#         k = Vet("john", 21, 200)
#         self.assertEqual(k.name, "john")
#         self.assertEqual(k.age, 21)
#         self.assertEqual(k.salary, 200)
#
#     def test_vet_repr(self):
#         k = Vet("ally", 36, 190)
#         res = str(k)
#         self.assertEqual(res, "Name: ally, Age: 36, Salary: 190")
#
#     def test_caretaker_init(self):
#         k = Caretaker("john", 21, 200)
#         self.assertEqual(k.name, "john")
#         self.assertEqual(k.age, 21)
#         self.assertEqual(k.salary, 200)
#
#     def test_caretaker_repr(self):
#         k = Caretaker("ally", 36, 190)
#         res = str(k)
#         self.assertEqual(res, "Name: ally, Age: 36, Salary: 190")
#
#     def test_zoo_init(self):
#         z = Zoo("My Zoo", 1500, 6, 10)
#         self.assertEqual(z._Zoo__animal_capacity, 6)
#         self.assertEqual(z._Zoo__workers_capacity, 10)
#         self.assertEqual(z._Zoo__budget, 1500)
#         self.assertEqual(z.name, "My Zoo")
#         self.assertEqual(z.animals, [])
#         self.assertEqual(z.workers, [])
#
#     def test_zoo_add_animal_success(self):
#         z = Zoo("My Zoo", 1500, 6, 10)
#         res = z.add_animal(Lion("Neo", "Male", 2), 1000)
#         self.assertEqual(res, "Neo the Lion added to the zoo")
#         self.assertEqual(len(z.animals), 1)
#         self.assertEqual(z._Zoo__budget, 500)
#
#     def test_zoo_add_animal_no_budget(self):
#         z = Zoo("My Zoo", 500, 6, 10)
#         res = z.add_animal(Lion("Neo", "Male", 2), 1000)
#         self.assertEqual(res, "Not enough budget")
#         self.assertEqual(len(z.animals), 0)
#         self.assertEqual(z._Zoo__budget, 500)
#
#     def test_zoo_add_animal_no_space(self):
#         z = Zoo("My Zoo", 1500, 0, 10)
#         res = z.add_animal(Lion("Neo", "Male", 2), 1000)
#         self.assertEqual(res, "Not enough space for animal")
#         self.assertEqual(len(z.animals), 0)
#         self.assertEqual(z._Zoo__budget, 1500)
#
#     def test_zoo_hire_worker_success(self):
#         z = Zoo("Some Zoo", 1500, 1, 1)
#         res = z.hire_worker(Vet("I am Vet", 20, 500))
#         self.assertEqual(res, "I am Vet the Vet hired successfully")
#         self.assertEqual(len(z.workers), 1)
#         self.assertEqual(z._Zoo__workers_capacity, 1)
#
#     def test_zoo_hire_worker_no_space(self):
#         z = Zoo("Some Zoo", 1500, 1, 0)
#         res = z.hire_worker(Vet("I am Vet", 20, 500))
#         self.assertEqual(res, "Not enough space for worker")
#         self.assertEqual(len(z.workers), 0)
#         self.assertEqual(z._Zoo__workers_capacity, 0)
#
#     def test_zoo_fire_worker_success(self):
#         z = Zoo("Zoo", 1500, 1, 1)
#         z.hire_worker(Keeper("K", 45, 100))
#         res = z.fire_worker("K")
#         self.assertEqual(res, "K fired successfully")
#         self.assertEqual(z.workers, [])
#
#     def test_zoo_fire_worker_unsuccessful(self):
#         z = Zoo("Zoo", 1500, 1, 1)
#         res = z.fire_worker("K")
#         self.assertEqual(res, "There is no K in the zoo")
#         self.assertEqual(z.workers, [])
#
#     def test_zoo_pay_worker_success(self):
#         z = Zoo("Zoo", 1500, 2, 2)
#         z.hire_worker(Vet("John", 23, 100))
#         z.hire_worker(Keeper("Bill", 28, 150))
#         res = z.pay_workers()
#         self.assertEqual(z._Zoo__budget, 1250)
#         self.assertEqual(res, "You payed your workers. They are happy. Budget left: 1250")
#
#     def test_zoo_pay_worker_no_budget(self):
#         z = Zoo("Zoo", 200, 2, 2)
#         z.hire_worker(Vet("John", 23, 100))
#         z.hire_worker(Keeper("Bill", 28, 150))
#         res = z.pay_workers()
#         self.assertEqual(res, "You have no budget to pay your workers. They are unhappy")
#
#     def test_zoo_tend_animal_success(self):
#         z = Zoo("Zoo", 500, 2, 2)
#         z.add_animal(Lion("John", "m", 2), 100)
#         z.add_animal(Tiger("Bill", "f", 4), 100)
#         res = z.tend_animals()
#         self.assertEqual(z._Zoo__budget, 205)
#         self.assertEqual(res, "You tended all the animals. They are happy. Budget left: 205")
#
#     def test_zoo_tend_animal_no_budget(self):
#         z = Zoo("Zoo", 250, 2, 2)
#         z.add_animal(Lion("John", "m", 2), 100)
#         z.add_animal(Tiger("Bill", "f", 4), 100)
#         res = z.tend_animals()
#         self.assertEqual(res, "You have no budget to tend the animals. They are unhappy.")
#
#     def test_zoo_profit(self):
#         z = Zoo("Mine", 250, 2, 2)
#         z.profit(250)
#         self.assertEqual(z._Zoo__budget, 500)
#
#     def test_animal_status(self):
#         z = Zoo("My Zoo", 500, 3, 3)
#         z.add_animal(Lion("Leo", "Male", 3), 100)
#         z.add_animal(Tiger("Tigy", "Female", 4), 100)
#         z.add_animal(Cheetah("Chi", "Female", 2), 100)
#         res = z.animals_status()
#         self.assertEqual(res,
#                          "You have 3 animals\n----- 1 Lions:\nName: Leo, Age: 3, Gender: Male\n----- 1 Tigers:\nName: Tigy, Age: 4, Gender: Female\n----- 1 Cheetahs:\nName: Chi, Age: 2, Gender: Female")
#
#     def test_worker_status(self):
#         z = Zoo("My Zoo", 500, 3, 3)
#         z.hire_worker(Vet("Leo", 35, 100))
#         z.hire_worker(Keeper("Tigy", 40, 100))
#         z.hire_worker(Caretaker("Chi", 24, 100))
#         res = z.workers_status()
#         self.assertEqual(res,
#                          "You have 3 workers\n----- 1 Keepers:\nName: Tigy, Age: 40, Salary: 100\n----- 1 Caretakers:\nName: Chi, Age: 24, Salary: 100\n----- 1 Vets:\nName: Leo, Age: 35, Salary: 100")
#
#
# if __name__ == "__main__":
#     unittest.main()


#
# from project.caretaker import Caretaker
# from project.cheetah import Cheetah
# from project.keeper import Keeper
# from project.lion import Lion
# from project.tiger import Tiger
# from project.vet import Vet
# # from project.zoo import Zoo
#
#
# zoo = Zoo("Zootopia", 3000, 5, 8)
#
# # Animals creation
# animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion("Simba", "Male", 4), Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]
#
# # Animal prices
# prices = [200, 190, 204, 156, 211, 140]
#
# # Workers creation
# workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68), Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280), Vet("Sam", 29, 220)]
#
# # Adding all animals
# for i in range(len(animals)):
#     animal = animals[i]
#     price = prices[i]
#     print(zoo.add_animal(animal, price))
#
# # Adding all workers
# for worker in workers:
#     print(zoo.hire_worker(worker))
#
# # Tending animals
# print(zoo.tend_animals())
#
# # Paying keepers
# print(zoo.pay_workers())
#
# # Fireing worker
# print(zoo.fire_worker("Adam"))
#
# # Printing statuses
# print(zoo.animals_status())
# print(zoo.workers_status())























# from project.worker import Worker
# from project.animal import Animal
# from project.lion import Lion
# from project.tiger import Tiger
# from project.cheetah import Cheetah
# from project.keeper import Keeper
# from project.vet import Vet
# from project.caretaker import Caretaker
# class Zoo:
#     def __init__(self, name, budget, animal_capacity, workers_capacity):
#         self.name = name
#         self.__budget = budget
#         self.__animal_capacity= animal_capacity
#         self.__workers_capacity = workers_capacity
#         self.animals = []
#         self.workers = []
#     def add_animal(self, animal, price):
#         if len(self.animals) < self.__animal_capacity and self.__budget >= price:
#             self.animals.append(animal)
#             self.__budget -= price
#             return f"{animal.name} the {type(animal).__name__} added to the zoo"
#         if len(self.animals) < self.__animal_capacity and self.__budget < price:
#             return "Not enough budget"
#         return "Not enough space for animal"
#     def hire_worker(self, worker):
#         if len(self.workers) < self.__workers_capacity:
#             self.workers.append(worker)
#             return f"{worker.name} the {type(worker).__name__} hired successfully"
#         return "Not enough space for worker"
#
#     def fire_worker(self, worker_name):
#         for worker in self.workers:
#             if worker.name == worker_name:
#                 self.workers.remove(worker)
#                 return f"{worker_name} fired successfully"
#         return f"There is no {worker_name} in the zoo"
#
#     def pay_workers(self):
#         # total_salaries = 0
#         # for worker in self.workers:
#         #     total_salaries += worker.salary
#         total_salaries = sum(map(lambda worker: worker.salary, self.workers))
#
#         if total_salaries <= self.__budget:
#             self.__budget -= total_salaries
#             return f"You payed your workers. They are happy. Budget left: {self.__budget}"
#         return "You have no budget to pay your workers. They are unhappy"
#
#     def tend_animals(self):
#         total_money_for_care = sum(map(lambda animal: animal.money_for_care, self.animals))
#         if total_money_for_care <= self.__budget:
#             self.__budget -= total_money_for_care
#             return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
#         return "You have no budget to tend the animals. They are unhappy."
#
#     def profit(self ,amount):
#         self.__budget += amount
#
#     def animals_status(self):
#         result = f"You have {len(self.animals)} animals\n"
#
#         total_lions = 0
#         lions_info = []
#         for animal in self.animals:
#             if type(animal) == Lion:
#                 total_lions += 1
#                 lions_info.append(repr(animal))
#
#         total_tigers = 0
#         tigers_info = []
#         for animal in self.animals:
#             if type(animal) == Tiger:
#                 total_tigers += 1
#                 tigers_info.append(repr(animal))
#
#         total_cheetahs = 0
#         cheetahs_info = []
#         for animal in self.animals:
#             if type(animal) == Cheetah:
#                 total_cheetahs += 1
#                 cheetahs_info.append(repr(animal))
#
#         result += f"----- {total_lions} Lions:\n"
#         lions_result = "\n".join(lions_info)
#         result += lions_result + "\n"
#
#         result += f"----- {total_tigers} Tigers:\n"
#         tigers_result = "\n".join(tigers_info)
#         result += tigers_result + "\n"
#
#         result += f"----- {total_cheetahs} Cheetahs:\n"
#         cheetahs_result = "\n".join(cheetahs_info)
#         result += cheetahs_result
#
#         return result
#
#     def workers_status(self):
#         result = f"You have {len(self.workers)} workers\n"
#
#         total_keepers = 0
#         keepers_info = []
#         for worker in self.workers:
#             if type(worker) == Keeper:
#                 total_keepers += 1
#                 keepers_info.append(repr(worker))
#
#         total_caretakers = 0
#         caretakers_info = []
#         for worker in self.workers:
#             if type(worker) == Caretaker:
#                 total_caretakers += 1
#                 caretakers_info.append(repr(worker))
#
#         total_vets = 0
#         vets_info = []
#         for worker in self.workers:
#             if type(worker) == Vet:
#                 total_vets += 1
#                 vets_info.append(repr(worker))
#
#
#         result += f"----- {total_keepers} Keepers:\n"
#         keepers_result = "\n".join(keepers_info)
#         result += keepers_result + "\n"
#
#         result += f"----- {total_caretakers} Caretakers:\n"
#         caretakers_result = "\n".join(caretakers_info)
#         result += caretakers_result + "\n"
#
#         result += f"----- {total_vets} Vets:\n"
#         vets_result = "\n".join(vets_info)
#         result += vets_result
#
#         return result
#
