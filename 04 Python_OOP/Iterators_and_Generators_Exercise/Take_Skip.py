class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.current_num = 0
        self.nums_count = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.nums_count <= self.count:
            temp = self.current_num
            self.current_num += self.step
            self.nums_count += 1
            return temp
        raise StopIteration()

numbers = take_skip(2, 6)
for number in numbers:
    print(number)

numbers = take_skip(10, 5)
for number in numbers:
    print(number)

