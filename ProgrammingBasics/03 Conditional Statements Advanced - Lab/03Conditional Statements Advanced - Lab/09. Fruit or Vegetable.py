# •	Плодовете "fruit" имат следните възможни стойности:  banana, apple, kiwi, cherry, lemon и grapes;
# •	Зеленчуците "vegetable" имат следните възможни стойности:  tomato, cucumber, pepper и carrot;
# •	Всички останали са "unknown".
name = input()
if name == 'banana' or name == 'apple' or name == 'kiwi' or name == 'cherry' or name == 'lemon' or name == 'grapes':
    print('fruit')
elif name == 'tomato' or name == 'cucumber' or name == 'pepper' or name == 'carrot':
    print('vegetable')
else:
    print('unknown')