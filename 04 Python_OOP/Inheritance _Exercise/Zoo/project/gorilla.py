from project.mammal import Mammal

class Gorilla(Mammal):
    def __init__(self, name):
        super().__init__(name)
    
# gorilla = Gorilla("Stella")
# print(gorilla.__class__.__bases__[0].__name__)
# print(gorilla.name)
