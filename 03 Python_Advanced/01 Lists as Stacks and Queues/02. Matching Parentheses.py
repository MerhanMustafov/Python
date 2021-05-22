expression = input()
parentheses_indices = []
for i in range(len(expression)):
    if expression[i] == "(":
        parentheses_indices.append(i)
    elif expression[i] == ")":
        print(expression[parentheses_indices.pop():i+1])


# expression = input()
#
# s = []
# for i in range(len(expression)):
#     ch = expression[i]
#     if ch == '(':
#         s.append(i)
#     elif ch == ')':
#         j = s.pop()
#         print(expression[j:i+1])