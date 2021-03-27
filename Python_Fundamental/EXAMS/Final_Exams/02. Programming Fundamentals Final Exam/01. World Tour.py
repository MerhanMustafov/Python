stops = input()
# print(stops)

command = input()
while not command == "Travel":
    command = command.split(":")
    if command[0] == "Add Stop":
        index = int(command[1])
        string = command[2]
        if 0 <= index < len(stops):
            stops = stops[:index] + string + stops[index:]
    elif command[0] == "Remove Stop":
        start_index = int(command[1])
        end_index = int(command[2])
        if 0 <= start_index < len(stops) and 0 <= end_index < len(stops):
            stops = stops[:start_index] + stops[end_index+1:]
    elif command[0] == "Switch":
        old_str = command[1]
        new_str = command[2]
        if old_str in stops:
            stops = stops.replace(old_str, new_str)

    print(stops)
    command = input()
print(f"Ready for world tour! Planned stops: {stops}")