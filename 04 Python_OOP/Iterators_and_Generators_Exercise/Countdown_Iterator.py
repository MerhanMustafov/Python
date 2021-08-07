class countdown_iterator:
    def __init__(self, count):
        self.count = count
        self.current_iter = self.count

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_iter >= 0:
            temp = self.current_iter
            self.current_iter -= 1
            return temp
        raise StopIteration()

iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")



