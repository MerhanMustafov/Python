start = int(input())
end = int(input())
magic_number = int(input())
counter = 0
is_found = False
for first_num in range(start, end + 1):
    for sec_num in range(start, end + 1):
        counter += 1
        if first_num + sec_num == magic_number:
            print(f"Combination N:{counter} ({first_num} + {sec_num} = {magic_number})")
            is_found = True
            break
    if is_found:
        break

if not is_found:
    print(f"{counter} combinations - neither equals {magic_number}")
