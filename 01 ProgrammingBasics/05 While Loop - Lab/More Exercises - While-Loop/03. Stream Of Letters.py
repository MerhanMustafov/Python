command = input()
n = 0
o = 0
c = 0
word = ''
while command != 'End':
    if ord(command) in range(65,91) or ord(command) in range(97,123):

        if command == 'n' and n == 0:
            n+=1
            command = input()
            continue
        elif command == 'o' and o == 0:
            o+=1
            command = input()
            continue
        elif command == 'c' and c == 0:
            c+=1
            command = input()
            continue
        if n == 1 and o == 1 and c == 1:
            print(f'{word}', end=' ')
            n = 0
            o = 0
            c = 0
            word = ''
            continue
        word += command
        command = input()
    else:
        command = input()
        continue
if command == 'End' and n == 1 and o == 1 and c == 1:
    print(f'{word}', end=' ')