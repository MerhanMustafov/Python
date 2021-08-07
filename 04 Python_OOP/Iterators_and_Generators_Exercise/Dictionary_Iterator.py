class dictionary_iter:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.keys = list(self.dictionary.keys())
        self.current_key = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_key <= len(self.keys)-1:
            cur = self.current_key
            self.current_key += 1
            result_tuple = (self.keys[cur], self.dictionary[self.keys[cur]])
            return result_tuple
        raise StopIteration()
result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
