# import re
# text = input()
#
# pattern = r"\+359( |-)2\1\d{3}\1\d{4}\b"
# valid_num = [obj.group() for obj in re.finditer(pattern, text)]
# print(", ".join(valid_num))
import re
pattern = r"\+359 2 [0-9]{3} [0-9]{4}|\+359-2-[0-9]{3}-[0-9]{4}\b"
numbers = input()
x = re.findall(pattern, numbers)
print(", ".join(x))