import datetime
class DVD:
    def __init__(self, name: str, id: int,
     creation_year: int,
      creation_month: str,
       age_restriction: int):
        self.name = str(name)
        self.id = int(id)
        self.creation_year = int(creation_year)
        self.creation_month = str(creation_month)
        self.age_restriction = int(age_restriction)
        self.is_rented = False
    def int2month(month: int) -> str:
        month_str = datetime.date(1900, int(month), 1).strftime("%B")
        return month_str
    @classmethod
    def from_date(cls, id: int, name: str, date: str, age_restriction: int):
        date = date.split(".")
        month = cls.int2month(int(date[1])) 
        return cls(name, id, int(date[2]), month, age_restriction)
    def __repr__(self):
        status = "rented" if self.is_rented else "not rented"
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction {self.age_restriction}. Status: {status}"