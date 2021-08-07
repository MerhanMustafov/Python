class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.end_num = number
        self.cur_idx = 0
        self.start_num = 0

    def __iter__(self):
        return self
    def __next__(self):
        lst = list(self.sequence)
        while self.start_num < self.end_num:
            if self.cur_idx == len(lst):
                self.cur_idx = 0
            temp = self.cur_idx
            self.cur_idx += 1
            self.start_num += 1
            return lst[temp]

        raise StopIteration()

result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')


