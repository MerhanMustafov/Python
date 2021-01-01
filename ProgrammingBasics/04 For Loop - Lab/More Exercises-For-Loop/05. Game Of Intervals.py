n = int(input())
interval1 = 0
interval2 = 0
interval3 = 0
interval4 = 0
interval5 = 0
invalid = 0
result = 0


for numbers in range (0, n):
    input_number = float(input())
    if 0 <= input_number <= 9:
        result += (input_number * 0.2)
        interval1 += 1
        pass
    elif 10 <= input_number <= 19:
        result += (input_number * 0.3)
        interval2 += 1
        pass
    elif 20 <= input_number <= 29:
        result += (input_number * 0.4)
        interval3 += 1
        pass
    elif 30 <= input_number <= 39:
        result += 50
        interval4 += 1
        pass
    elif 40 <= input_number <= 50:
        result += 100
        interval5 += 1
        pass
    else:
        result /= 2
        invalid += 1
        pass
print(f'{result:.2f}')
print(f'From 0 to 9: {interval1 * 10:.2f}%')
print(f'From 10 to 19: {interval2 * 10:.2f}%')
print(f'From 20 to 29: {interval3 * 10:.2f}%')
print(f'From 30 to 39: {interval4 * 10:.2f}%')
print(f'From 40 to 50: {interval5 * 10:.2f}%')
print(f'Invalid numbers: {invalid * 10:.2f}%')