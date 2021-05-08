string = input()

command = input()
while not command == "Generate":
    command = command.split(">>>")
    if command[0] == "Contains":
        substring = command[1]
        if substring in string:
            print(f"{string} contains {substring}")
        else:
            print("Substring not found!")
    elif command[0] == "Flip":
        up_low = command[1]
        start = int(command[2])
        end = int(command[3])
        if up_low == "Upper":
            upper = string[start:end].upper()
            string = string.replace(string[start:end], upper)
        elif up_low == "Lower":
            lower = string[start:end].lower()
            string = string.replace(string[start:end], lower)
        print(string)
    elif command[0] == "Slice":
        start = int(command[1])
        end = int(command[2])
        string = string.replace(string[start:end], "")
        print(string)

    command = input()
print(f"Your activation key is: {string}")