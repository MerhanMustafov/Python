n = int(input())

for a in range(0, n):
    letter1 = chr(97 + a)
    for b in range(0, n ):
        letter2 = chr(97 + b)
        for c in range(0, n):
            letter3 = chr(97 + c)
            print(f"{letter1}{letter2}{letter3}")
# n = int(input())
#
# for first_char in range(97, 97 + n):
#     for second_char in range(97, 97 + n):
#         for third_char in range(97, 97 + n):
#             print(f"{chr(first_char)}{chr(second_char)}{chr(third_char)}")
#
