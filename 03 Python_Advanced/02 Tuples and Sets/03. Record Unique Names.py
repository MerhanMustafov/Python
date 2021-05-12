def input_to_list(count):
    lines = []
    for _ in range(count):
        lines.append(input())
    return lines

def print_resut(names):
    for name in names:
        print(name)
n = int(input())
names = input_to_list(n)
# names = ['Lyle'
# 'Bruce'
# 'Alice'
# 'Easton'
# 'Shawn'
# 'Alice'
# 'Shawn'
# ]
unique_names = set(names)
print_resut(unique_names)


