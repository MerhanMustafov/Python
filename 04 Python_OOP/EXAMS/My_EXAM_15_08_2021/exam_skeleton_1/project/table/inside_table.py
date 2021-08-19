# from project.table.outside_table import OutsideTable
from project.table.table import Table


class InsideTable(Table):
    def __init__(self, table_number, capacity):
        super().__init__(table_number, capacity)

    @property
    def table_number(self):
        return self.__table_number

    @table_number.setter
    def table_number(self, value):
        if not 1 <= value <= 50:
            raise ValueError("Inside table's number must be between 1 and 50 inclusive!")

        self.__table_number = value

# inside_table = InsideTable(51, 10)
# print(inside_table.table_number)

# inside_table = InsideTable(1, 3)
# outside_table = OutsideTable(51, 7)
# print(inside_table.free_table_info())
# print(outside_table.free_table_info())

