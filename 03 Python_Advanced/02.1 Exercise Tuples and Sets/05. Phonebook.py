command = input()
phone_book = {}
while not command.isdigit():
    command = command.split("-")
    phone_book[command[0]] = command[1]

    command = input()
n = int(command)
for _ in range(n):
    name = input()
    if name in phone_book:
        print(f"{name} -> {phone_book[name]}")
    else:
        print(f"Contact {name} does not exist.")
# for k, v in phone_book.items():
#     if k in phone_book:
#         print(f"{k} -> {v}")
#     else:
#         print(f"Contact {k} does not exist.")

