class EncryptionGenerator:
    def __init__(self, text: str):
        self.text = text
    def __add__(self, other):
        if not isinstance(other, (float, int)):
            raise ValueError("You must add a number.")
        result = ""
        for el in self.text:
            num = ord(el) + other
            while num < 32:
                num += 95
            while num > 126:
                num -= 95
            result += chr(num)
            
        return result
some_text = EncryptionGenerator('I Love Python!')
print(some_text + 1)
print(some_text + (-1))
example = EncryptionGenerator('Super-Secret Message')
print(example + 20)
print(example + (-52))

