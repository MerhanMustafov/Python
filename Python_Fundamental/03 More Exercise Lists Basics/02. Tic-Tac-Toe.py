import sys
lst_1 = input().split(" ")
lst_2 = input().split(" ")
lst_3 = input().split(" ")
count = 0
won_first = False
won_second = False
draw = False
if "0" not in lst_1:
    if lst_1[0] == 1:
        won_first = True
    else:
        won_second = True
elif "0" not in lst_2:
    if lst_2[0] == 1:
        won_first = True
    else:
        won_second = True
elif "0" not in lst_3:
    if lst_3[0] == 1:
        won_first = True
    else:
        won_second = True
if lst_2[1] == (lst_1[0] and lst_3[2]) or lst_2[1] == (lst_1[2]):
    if lst_2[1] == "1":
            won_first = True
    elif lst_2[1] == "2":
        won_second = True
    else:
        draw = True


else:
    draw = True
# else:
#     for i in range(len(lst_1)):
#         new1 = lst_1[i]
#         new2 = lst_2[i]
#         new3 = lst_3[i]
#         if new1 == new2 == new3:
#             if new1 == "1":
#                 won_first = True
#             elif new1 == "2":
#                 won_second = True
#             else:
#                 draw = True
#             break
#     if lst_2[1] == (lst_1[0] and lst_3[2]) or lst_2[1] == (lst_1[2] and lst_3[0]):
#         if lst_2[1] == "1":
#             won_first = True
#         elif lst_2[1] == "2":
#             won_second = True
#         else:
#             draw = True

if won_first:
    print("First player won")
elif won_second:
    print("Second player won")
elif draw:
    print("Draw!")
