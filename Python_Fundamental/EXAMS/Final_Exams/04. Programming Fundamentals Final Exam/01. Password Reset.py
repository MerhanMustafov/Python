string = input()

command = input()
while not command == "Done":
    command = command.split()
    if command[0] == "TakeOdd":
        string = string[1::2]
    elif command[0] == "Cut":
        index = int(command[1])
        length = int(command[2])
        substing = string[index:index+length]
        string = string.replace(substing, "", 1)
    elif command[0] == "Substitute":
        sub_str = command[1]
        substitute = command[2]
        if sub_str in string:
            string = string.replace(sub_str, substitute)
        else:
            print("Nothing to replace!")
            command = input()
            continue
    print(string)
    command = input()
print(f"Your password is: {string}")