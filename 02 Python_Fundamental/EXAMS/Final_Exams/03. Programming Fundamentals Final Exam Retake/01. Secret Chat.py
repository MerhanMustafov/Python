concealde_message = input()

command = input()
while not command == "Reveal":
    command = command.split(":|:")
    # print(command)
    if command[0] == "InsertSpace":
        index = int(command[1])
        concealde_message = concealde_message[:index] + " " + concealde_message[index:]
    elif command[0] == "Reverse":
        substring = command[1]
        if substring in concealde_message:
            concealde_message = concealde_message.replace(substring, "", 1)
            reversed_substring = substring[::-1]
            concealde_message = concealde_message[0:] + reversed_substring
        else:
            print("error")
            command = input()
            continue
    elif command[0] == "ChangeAll":
        sub = command[1]
        replacement = command[2]
        concealde_message = concealde_message.replace(sub, replacement)
    print(concealde_message)
    command = input()
print(f"You have a new text message: {concealde_message}")