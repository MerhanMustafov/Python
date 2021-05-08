n = int(input())
m = int(input())
size_of_the_cake = n * m
number_taken_pieces = 0
command = input()
left = True
while command != 'STOP':
    number = int(command)
    number_taken_pieces += number
    if number_taken_pieces >= size_of_the_cake:
        left = False
        break
    command = input()
if not left:
    left_pieces = abs(size_of_the_cake - number_taken_pieces)
    print(f"No more cake left! You need {left_pieces} pieces more.")
if command == 'STOP':
    print(f"{size_of_the_cake - number_taken_pieces} pieces are left.")




# width = int(input())
# length = int(input())
# total_prieces = width * length
# comand = input()
# while comand != "STOP":
#     current_pieces = int(comand)
#     total_prieces -= current_pieces
#     if total_prieces < 0:
#         break
#     comand = input()
# if total_prieces >= 0: # or if command == "STOP"
#     print(f"{total_prieces} pieces are left.")
# else:
#     print(f"No more cake left! You need {abs(total_prieces)} pieces more.")
#
