from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:
    def __init__(self, name):
        self.name = name

        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "" or value == " ":
            raise ValueError("Name cannot be empty string or white space!")

        self.__name = value

    def add_food (self, food_type, name, price):
        for food in self.food_menu:
            if food.name == name:
                raise Exception(f"{food_type} {name} is already in the menu!")
        food = None
        if food_type == "Bread":
            food = Bread(name, price)
        elif food_type == "Cake":
            food = Cake(name, price)
        self.food_menu.append(food)
        return f"Added {name} ({food_type}) to the food menu"

    def add_drink (self, drink_type, name, portion, brand):
        for drink in self.drinks_menu:
            if drink.name == name:
                raise Exception(f"{drink_type} {name} is already in the menu!")
        drink = None
        if drink_type == "Tea":
            drink = Tea(name, portion, brand)
        elif drink_type == "Water":
            drink = Water(name, portion, brand)
        self.drinks_menu.append(drink)
        return f"Added {name} ({brand}) to the drink menu"


    def add_table (self, table_type, table_number, capacity):
        for table in self.tables_repository:
            if table.table_number == table_number:
                raise Exception(f"Table {table_number} is already in the bakery!")

        table = None
        if table_type == "InsideTable":
            table = InsideTable(table_number, capacity)
        elif table_type == "OutsideTable":
            table = OutsideTable(table_number, capacity)
        self.tables_repository.append(table)
        return f"Added table number {table_number} in the bakery"

    def reserve_table (self, number_of_people):
        for table in self.tables_repository:
            if not table.is_reserved:
                if table.capacity >= number_of_people:
                    table.is_reserved = True
                    return f"Table {table.table_number} has been reserved for {number_of_people} people"

        return f"No available table for {number_of_people} people"

    # def order_food(self, table_number: int, *food_names):
    #     food_names = list(food_names)
    #     menue = [f.name for f in self.food_menu]
    #     ordered = []
    #     not_in_the_menue = []
    #
    #     for table in self.tables_repository:
    #         if table.table_number == table_number:
    #
    #             for food in self.food_menu:
    #                 if food.name in food_names:
    #                     ordered.append(food)
    #                     table.order_food(food)
    #
    #
    #             for f_name in food_names:
    #                 if f_name not in menue:
    #                     not_in_the_menue.append(f_name)
    #             result = ""
    #
    #             result += f"Table {table_number} ordered\n"
    #             for f in ordered:
    #                 result += f"{repr(f)}\n"
    #             if not_in_the_menue:
    #                 result += f"{self.name} does not have in the menu:\n"
    #                 for ff in not_in_the_menue:
    #                     result += f"{ff}\n"
    #             return result[:-1]
    #
    #     return f"Could not find table {table_number}"
    #
    #
    #
    #
    # def order_drink (self, table_number, *drinks_name):
    #     drinks_name = list(drinks_name)
    #     menue = [d.name for d in self.drinks_menu]
    #     ordered = []
    #     not_in_the_menue = []
    #
    #     for table in self.tables_repository:
    #         if table.table_number == table_number:
    #
    #             for drink in self.drinks_menu:
    #                 if drink.name in drinks_name:
    #                     ordered.append(drink)
    #                     table.order_drink(drink)
    #
    #
    #             for d_name in drinks_name:
    #                 if d_name not in menue:
    #                     not_in_the_menue.append(d_name)
    #             result = ""
    #
    #             result += f"Table {table_number} ordered\n"
    #             for d in ordered:
    #                 result += f"{repr(d)}\n"
    #             if not_in_the_menue:
    #                 result += f"{self.name} does not have in the menu:\n"
    #                 for dd in not_in_the_menue:
    #                     result += f"{dd}\n"
    #             return result[:-1]
    #
    #     return f"Could not find table {table_number}"
    def order_food(self, table_number: int, *args):
        table = [t for t in self.tables_repository if t.table_number == table_number]
        if table:
            table = table[0]
            food_not_in_menu = []
            for food_name in args:
                is_found = False
                for food in self.food_menu:
                    if food.name == food_name:
                        table.order_food(food)
                        is_found = True
                        break
                if not is_found:
                    food_not_in_menu.append(food_name)

            result = f"Table {table.table_number} ordered:\n"
            for food in table.food_orders:
                result += f"{repr(food)}\n"
            if food_not_in_menu:
                result += f"{self.name} does not have in the menu:\n"
                for food in food_not_in_menu:
                    result += f"{food}\n"

            return result

        return f"Could not find table {table_number}"

    def order_drink(self, table_number: int, *args):
        table = [t for t in self.tables_repository if t.table_number == table_number]
        if table:
            table = table[0]
            drinks_not_in_menu = []
            for drink_name in args:
                is_found = False
                for drink in self.drinks_menu:
                    if drink.name == drink_name:
                        table.order_drink(drink)
                        is_found = True
                        break
                if not is_found:
                    drinks_not_in_menu.append(drink_name)

            result = f"Table {table.table_number} ordered:\n"
            for drink in table.drink_orders:
                result += f"{repr(drink)}\n"
            if drinks_not_in_menu:
                result += f"{self.name} does not have in the menu:\n"
                for drink in drinks_not_in_menu:
                    result += f"{drink}\n"

            return result

        return f"Could not find table {table_number}"

    def leave_table(self, table_number):
        for table in self.tables_repository:
            if table.table_number == table_number:
                table_bill = table.get_bill()
                table.clear()
                result = f"Table: {table_number}\n"
                result += f"Bill: {table_bill:.2f}"
                self.total_income += table_bill
                return result

    def get_free_tables_info(self):
        result = ""
        for table in self.tables_repository:
            if not table.is_reserved:
                result += table.free_table_info() + "\n"

        return result[:-1]

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"
