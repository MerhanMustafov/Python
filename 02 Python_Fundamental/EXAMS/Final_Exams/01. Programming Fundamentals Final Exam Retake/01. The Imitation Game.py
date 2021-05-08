encrypted_message = input()
# print(encrypted_message)
command = input()
while not command == "Decode":
    command = command.split("|")
    if command[0] == "Move":
        n_letters = int(command[1])
        encrypted_message = encrypted_message[n_letters:] + encrypted_message[:n_letters]
    elif command[0] == "Insert":
        index = int(command[1])
        value = command[2]
        encrypted_message = encrypted_message[:index] + value + encrypted_message[index:]
    elif command[0] == "ChangeAll":
        replace_that = command[1]
        with_that = command[2]
        while replace_that in encrypted_message:
            encrypted_message = encrypted_message.replace(replace_that, with_that)
    command = input()
print(f"The decrypted message is: {encrypted_message}")