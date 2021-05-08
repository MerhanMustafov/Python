# text = input()
#
# sum = 0
# while text != "NoMoreMoney":
#     number = float(text)
#     if number  < 0:
#         print('Invalid operation!')
#         break
#     else:
#         print(f'Increase: {number:.2f}')
#         sum += number
#     text = input()
#
# print(f'Total: {sum:.2f}')

text = input()

sum = 0
while text != "NoMoreMoney":
    number = float(text)

    if number  <= 0:
        print('Invalid operation!')
        break
    else:
        print(f'Increase: {number:.2f}')
        sum += number
    text = input()

print(f'Total: {sum}')