from project.animal import Animal

class Reptile(Animal):
    def __init__(self, name):
        super().__init__(name)
    
# reptile = Reptile("Stella")
# print(reptile.__class__.__bases__[0].__name__)
# print(reptile.name)
