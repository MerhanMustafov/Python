string = input().strip()

command = input()
while not command == "Finish":
    command = command.split()
    if command[0] == "Replace":
        charr, new = command[1], command[2]
        string = string.replace(charr, new)
        print(string)

    elif command[0] == "Cut":
        start = int(command[1])
        end = int(command[2])
        if  not 0 <= start < len(string):
            print(f"Invalid indices!")
        elif not 0 <= end < len(string):
            print(f"Invalid indices!")
        else:
            sub = string[start:end+1]
            string = string.replace(sub, '', 1)
            print(string)

    elif command[0] == "Make":
        upper_lower = command[1]
        if upper_lower == "Upper":
            string = string.upper()
        elif upper_lower == "Lower":
            string = string.lower()
        print(string)

    elif command[0] == "Check":
        for_check = command[1]
        if for_check in string:
            print(f"Message contains {for_check}")
        else:
            print(f"Message doesn't contain {for_check}")

    elif command[0] == "Sum":
        start = int(command[1])
        end = int(command[2])
        if  0 <= start < len(string) and 0 <= end < len(string):
            substr = string[start:end+1]
            total = [ord(x) for x in substr]
            total = sum(total)
            print(total)
        else:
            print("Invalid indices!")
    command = input()