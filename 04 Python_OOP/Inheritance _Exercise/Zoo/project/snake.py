from project.reptile import Reptile

class Snake(Reptile):
    def __init__(self, name):
        super().__init__(name)
    
# snake = Snake("Stella")
# print(snake.__class__.__bases__[0].__name__)
# print(snake.name)
