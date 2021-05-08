number = int(input())
number_for_printing = 1
all_is_printed = False
for row in range(1,number+1):
    for colomn in range(1, row + 1):
        print(f'{number_for_printing}', end=' ')
        number_for_printing += 1
        if number_for_printing > number:
            all_is_printed = True
            break
    if all_is_printed:
        break
    print()

