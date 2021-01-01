total_sold_tickets = 0
total_students_tickets = 0
total_standard_tickets = 0
total_kids_tickets = 0
command = input()
while command != 'Finish':
    movie_name = command
    tickets_for_sale = int(input())
    sold_tickets_for_sold_movie = 0

    while sold_tickets_for_sold_movie < tickets_for_sale:
        type_of_the_tickets = input()
        if type_of_the_tickets == 'End':
            break
        elif type_of_the_tickets == 'student':
            total_students_tickets += 1
        elif type_of_the_tickets == 'standard':
            total_standard_tickets += 1
        elif type_of_the_tickets == 'kid':
            total_kids_tickets += 1
        sold_tickets_for_sold_movie += 1
        total_sold_tickets += 1

    percent_of_full_haul = sold_tickets_for_sold_movie / tickets_for_sale * 100
    print(f"{movie_name} - {percent_of_full_haul:.2f}% full.")
    command = input()
print(f"Total tickets: {total_sold_tickets}")
percent_of_students_tickets = total_students_tickets / total_sold_tickets * 100
percent_of_standard_tickets = total_standard_tickets / total_sold_tickets * 100
percent_of_kids_tickets = total_kids_tickets / total_sold_tickets * 100
print(f'{percent_of_students_tickets:.2f}% student tickets.')
print(f'{percent_of_standard_tickets:.2f}% standard tickets.')
print(f'{percent_of_kids_tickets:.2f}% kids tickets.')

