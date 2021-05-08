# text = input()
# sum = 0
#
# for symbol in text:
#     if symbol == "a":
#         sum+=1
#     elif symbol == "e":
#         sum += 2
#     elif symbol == "i":
#         sum += 3
#     elif symbol == "o":
#         sum += 4
#     elif symbol == "u":
#         sum += 5
# print(sum)

input_text_by_me = input()
sum = 0
for letters in range(0, len(input_text_by_me)):
    position = input_text_by_me[letters]
    if position == 'a':
        sum+=1
    if position == 'e':
        sum += 2
    if position == 'i':
        sum += 3
    if position =='o':
        sum+= 4
    if position == 'u':
        sum+= 5
print(sum)