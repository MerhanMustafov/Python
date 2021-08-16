from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:
    def __init__(self, name):
        self.name = name

        # that will contain every type
        # of food in the bakery's menu.
        self.food_menu = []
        # that will contain every type
        # of drink in the bakery's menu.
        self.drinks_menu = []
        # list containing every table at the bakery.
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

    def add_food(self, food_type: str, name, price):
        if food_type == "Bread":
            bread = Bread(name, price)
            if bread in self.food_menu:
                raise Exception(f"{food_type} {name} is already in the menu!")
            self.food_menu.append(bread)
            return f"Added {name} ({food_type}) to the food menu"
        if food_type == "Cake":
            cack = Cake(name, price)
            if cack in self.food_menu:
                raise Exception(f"{food_type} {name} is already in the menu!")

            self.food_menu.append(cack)
            return f"Added {name} ({food_type}) to the food menu"




    def add_drink(self, drink_type: str, name, portion: int, brand):
        if drink_type == "Tea":
            tea = Tea(name, portion, brand)
            if tea in self.drinks_menu:
                raise Exception(f"{drink_type} {name} is already in the menu!")
            self.drinks_menu.append(tea)
            return f"Added {name} ({brand}) to the drink menu"
        if drink_type == "Water":
            water = Water(name, portion, brand)
            if water in self.food_menu:
                raise Exception(f"{drink_type} {name} is already in the menu!")

            self.drinks_menu.append(water)
            return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number, capacity):
        if table_type == "InsideTable":
            in_table = InsideTable(table_number, capacity)
            if in_table in self.tables_repository:
                raise Exception(f"{table_number} is already in the bakery!")
            self.tables_repository.append(in_table)
            return f"Added table number {table_number} in the bakery"
        if table_type == "OutsideTable":
            out_table = OutsideTable(table_number, capacity)
            if out_table in self.tables_repository:
                raise Exception(f"{table_number} is already in the bakery!")
            self.tables_repository.append(out_table)
            return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people):
        for table in self.tables_repository:
            if not table.is_reserved:
                if table.capacity >= number_of_people:
                    table.is_reserved = True
                    return f"Table {table.table_number} has been reserved for {number_of_people} people"
                return f"No available table for {number_of_people} people"

    def order_food(self, table_number, *food_name):
        foods = list(food_name)

        for table in self.tables_repository:
            if table.table_number == table_number:
                could_be_ordered = [food for food in self.food_menu if food.name in foods]
                # for food_c in could_be_ordered:
                #     self.total_income += food_c.price


                result = f"Table {table_number} ordered:\n"
                for f in could_be_ordered:
                    table.order_food(f)
                    result += f"- {f.name}: {f.portion}g - {f.price}lv\n"

                for f in self.food_menu:
                    if f.name in foods:
                        foods.remove(f.name)

                could_not_be_ordered = foods

                result += f"{self.name} does not have in the menu:\n"
                for fff in could_not_be_ordered:
                    result += f"{fff}\n"

                return result








        return f"Could not find table {table_number}"


    def order_drink(self, table_number, *drink_name):
        drinks = list(drink_name)
        for table in self.tables_repository:
            if table.table_number == table_number:
                could_be_ordered = [drink for drink in self.drinks_menu if drink.name in drinks]
                # for drink_c in could_be_ordered:
                #     self.total_income += drink_c.price

                result = f"Table {table_number} ordered:\n"
                for d in could_be_ordered:
                    table.order_drink(d)
                    result += f"- {d.name} {d.brand} - {d.portion}ml - {d.price}lv"

                for d in self.drinks_menu:
                    if d.name in drinks:
                        drinks.remove(d.name)

                could_not_be_ordered = drinks

                result += f"{self.name} does not have in the menu:\n"
                for ddd in could_not_be_ordered:
                    result += f"{ddd}\n"

                return result

        return f"Could not find table {table_number}"


    def leave_table(self, table_number):
        for table in self.tables_repository:
            if table.table_number == table_number:
                table_bill = table.get_bill()
                self.total_income += table_bill
                table.clear()
                return f"Table: {table_number}\n"\
                        f"Bill: {table_bill:.2f}"


    def get_free_tables_info(self):
        table_info = []
        for table in self.tables_repository:
            if not table.is_reserved:
                table_info.append(table.free_table_info())
        return "\n".join(table_info)

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"
