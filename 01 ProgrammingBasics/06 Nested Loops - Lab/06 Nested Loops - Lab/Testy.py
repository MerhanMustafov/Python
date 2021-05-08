film_name = input()
total_tickets = 0
student = 0
standerd = 0
kids = 0
while film_name != 'Finish':
    total_free_space = int(input())
    count = 0

    while total_free_space > count:
        type_ticket = input()
        if type_ticket == 'End':
            break
        elif type_ticket == 'student':
            student += 1
        elif type_ticket == 'standard':
            standerd += 1
        elif type_ticket == 'kid':
            kids += 1
        count += 1
        total_tickets += 1
    full_houl =count / total_free_space * 100
    print(f"{film_name} - {full_houl:.2f}% full.")
    film_name = input()

print(f"Total tickets: {total_tickets}")
print(f"{student / total_tickets * 100:.2f}% student tickets.")
print(f"{standerd / total_tickets * 100:.2f}% standard tickets.")
print(f"{kids / total_tickets * 100:.2f}% kids tickets.")