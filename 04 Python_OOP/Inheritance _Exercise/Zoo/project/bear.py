from project.mammal import Mammal

class Bear(Mammal):
    def __init__(self, name):
        super().__init__(name)
    
# bear = Bear("Bobi")
# print(bear.__class__.__bases__[0].__name__)
# print(bear.name)
