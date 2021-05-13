def fill_phone_book():
    command = input()
    phone_book = {}
    while not command.isdigit():
        command = command.split("-")
        phone_book[command[0]] = command[1]

        command = input()
    return phone_book, int(command)
def search_contact(contact_name, phone_book):
    if name in phone_book:
        print(f"{name} -> {phone_book[name]}")
    else:
        print(f"Contact {name} does not exist.")

phone_book, iterations_count  = fill_phone_book()
for _ in range(iterations_count):
    name = input()
    search_contact(name, phone_book)


