class EncryptionGenerator:
    def __init__(self, text):
        self.text = text

    def __add__(self, other):
        if not isinstance(other, int):
            raise ValueError("You must add a number.")

        result = list(self.text)
        for el in range(len(result)):
            ascii_el_num = ord(result[el])
            if 32 <= ascii_el_num <= 126:
                if ascii_el_num + other > 126:
                    ascii_el_num = (ascii_el_num + other) - 95
                elif ascii_el_num + other < 32:
                    ascii_el_num = (ascii_el_num + other) + 95
                else:
                    ascii_el_num += other
                result[el] = chr(ascii_el_num)

        return "".join(result)



# some_text = EncryptionGenerator('I Love Python!')
# print(some_text + 1)
# print(some_text + (-1))
# example = EncryptionGenerator('Super-Secret Message')
# print(example + 20)
# print(example + (-52))



