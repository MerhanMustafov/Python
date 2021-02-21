string = input().split("@")
string = list(map(int, string))

command = input()
position = 0

while not command == "Love!":
    jump, length = command.split()
    length = int(length)

    position += length

    if position < len(string):
        if string[position] == 0:
            print(f"Place {position} already had Valentine's day.")
            command = input()
            continue
        string[position] -= 2
        if string[position] == 0:
            print(f"Place {position} has Valentine's day.")
    else:
        position = 0
        if string[position] == 0:
            print(f"Place {position} already had Valentine's day.")
            command = input()
            continue
        string[position] -= 2
        if string[position] == 0:
            print(f"Place {position} has Valentine's day.")
    command = input()

count = 0
for x in string:
    if x > 0:
        count += 1
print(f"Cupid's last position was {position}.")
if count == 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {count} places.")