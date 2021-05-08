number_n = int(input())
capacity_p = int(input())
total_courses = 0
while number_n > 0:
    if number_n <= capacity_p:
        total_courses += 1
        break
    else:
        total_courses += number_n // capacity_p
        remains = number_n % capacity_p
        if remains > 0:
            total_courses += 1
            break
        else:
            break
print(total_courses)
