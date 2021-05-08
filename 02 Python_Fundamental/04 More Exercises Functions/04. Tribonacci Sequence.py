def tribonacci_sequence(num):
    start_list = [1, 1, 2]
    final_list = [1, 1, 2]
    result = ""

    if num == 2:
        return "1 1"
    if num == 1:
        return "1"

    for digit in range(3, num):
        last_digit = sum(start_list)

        start_list.pop(0)
        start_list.append(last_digit)
        final_list.append(last_digit)
    for l in range(len(final_list)):
        result += (str(final_list[l]) + " ")

    return result

num = int(input())
output = tribonacci_sequence(num)

print(output)