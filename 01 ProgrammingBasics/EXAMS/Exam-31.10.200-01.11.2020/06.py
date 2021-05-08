import sys
n = int(input())
is_valid = False
is_valid1 = False
for a in range(1, 9 + 1):
    for b in range(9, a - 1, -1):
        for c in range(1, 9 + 1):
            for d in range(9, c-1, - 1):
                derivative = a * b * c * d
                sum = a + b + c + d
                if derivative == sum and n % 10 == 5:
                    number_str = (f'{a}{b}{c}{d}')
                    is_valid = True
                if derivative // sum == 3 and n % 3 == 0:
                    number_str = (f'{d}{c}{b}{a}')
                    is_valid1 = True
                if is_valid:
                    number_str = (f'{a}{b}{c}{d}')
                    print(number_str)
                    sys.exit(0)

                elif is_valid1:
                    number_str1 = (f'{d}{c}{b}{a}')
                    print(number_str1)
                    sys.exit(0)
else:
    print(f'Nothing found')