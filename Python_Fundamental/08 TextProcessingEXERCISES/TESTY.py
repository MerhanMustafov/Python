string = input()
new_string = ""
explosions = 0

for index, char in enumerate(string):
    if explosions > 0:
        if char == ">":
            explosions += int(string[index + 1])
        else:
            explosions -= 1
            continue
    new_string += char
    if char == ">" and explosions == 0:
        explosions += int(string[index + 1])

print(new_string)