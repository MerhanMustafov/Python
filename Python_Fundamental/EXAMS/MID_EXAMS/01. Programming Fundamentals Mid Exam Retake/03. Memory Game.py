elements = input().split()

command = input()
number_of_moves = 0
while not command == "end" and len(elements) > 0:
    index_1, index_2 = command.split()
    index_1 = int(index_1)
    index_2 = int(index_2)
    number_of_moves += 1
    if index_1 == index_2 or (index_1 or index_2) >= len(elements) or (index_1 or index_2) < 0:
        middle_el_lst = len(elements) // 2
        for el in range(2):
            elements.insert(middle_el_lst, f"-{number_of_moves}a")
        print("Invalid input! Adding additional elements to the board")
    elif elements[index_1] == elements[index_2]:
        print(f"Congrats! You have found matching elements - {elements[index_1]}!")
        elements = [el for el in elements if not el == elements[index_1]]

    elif elements[index_1] != elements[index_2]:
        print("Try again!")
    command = input()

if len(elements) == 0:
    print(f"You have won in {number_of_moves} turns!")

else:
    print(f"Sorry you lose :(")
    for e in range(len(elements)):
        el = elements[e]
        print(f"{el}", end=" ")