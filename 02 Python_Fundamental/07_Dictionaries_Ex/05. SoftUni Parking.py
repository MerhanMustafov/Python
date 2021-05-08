n = int(input())
registrated = {}
unregistrated = []
command = input()
while n > 0:
    command = command.split()

    if command[0] == "register":
        user_name = command[1]
        plate_num = command[2]
        if user_name not in registrated:
            registrated[user_name] = plate_num
            print(f"{user_name} registered {plate_num} successfully")
        else:
            print(f"ERROR: already registered with plate number {plate_num}")
    elif command[0] == "unregister":
        user_name = command[1]
        if user_name in registrated:
            del registrated[user_name]
            print(f"{user_name} unregistered successfully")
        else:
            print(f"ERROR: user {user_name} not found")

    n -= 1
    if n == 0:
        break
    command = input()
for name, plate in registrated.items():
    print(f"{name} => {plate}")