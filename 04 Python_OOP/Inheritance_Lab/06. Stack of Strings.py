class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        self.data.append(element)
    def pop(self):
        last_el = self.data.pop()
        return last_el
    def top(self):
        return self.data[-1]
    def is_empty(self):
        return not self.data
    def __str__(self):
        return f"[{', '.join([d for d in self.data[::-1]])}]"