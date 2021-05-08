weight = int(input())
legth = int(input())
hight = int(input())
free_space = weight * legth * hight
whole_boxes = 0
command = input()
there_is_free_space = True
while command != 'Done':
    one_box = int(command)
    whole_boxes += one_box
    if free_space < whole_boxes:
        there_is_free_space = False
        needed = abs(free_space - whole_boxes)
        print(f"No more free space! You need {needed} Cubic meters more.")
        break
    command = input()
if there_is_free_space:
    print(f"{free_space - whole_boxes} Cubic meters left.")




# width = int(input())
# length = int(input())
# hight = int(input())
#
# count_free_space = width * length * hight
#
# comand = input()
#
# while comand != 'Done':
#     boxes = int(comand)
#     count_free_space -= boxes
#     if count_free_space <= 0:
#         print(f"No more free space! You need {abs(count_free_space)} Cubic meters more.")
#         break
#     comand = input()
# else:
#     print(f"{count_free_space} Cubic meters left.")
