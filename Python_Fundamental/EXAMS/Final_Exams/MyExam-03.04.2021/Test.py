string = input().strip()

command = input()
while not command == "Finish":

    command = command.split()
    if command[0] == "Replace":
        cur_char = command[1]
        new_char = command[2]
        while cur_char in string:
            string = string.replace(cur_char, new_char)
        print(string)
    elif command[0] == "Cut":
        start = int(command[1])
        end = int(command[2])
        if not 0 <= start < len(string):
            print(f"Invalid indices!")
        elif not 0 <= end < len(string):
            print(f"Invalid indices!")
        else:
            substr = string[start:end+1]
            string = string.replace(substr, '', 1)
            print(string)

    elif command[0] == "Make":
        upper_lower = command[1]
        if upper_lower == "Upper":
            string = string.upper()
        elif upper_lower == "Lower":
            string = string.lower()
        print(string)
    elif command[0] == "Check":
        to_check = command[1]
        if to_check in string.lower():
            print(f"Message contains {to_check}")
        else:
            print(f"Message doesn't contain {to_check}")
    elif command[0] == "Sum":
        start_ind = int(command[1])
        end_ind = int(command[2])
        if not 0 <= start_ind < len(string) and 0 <= end_ind < len(string):
            print("Invalid indices!")
        else:
            substring = string[start_ind: end_ind+1]
            summm = [ord(x) for x in substring]
            s = sum(summm)
            print(s)
    command = input()