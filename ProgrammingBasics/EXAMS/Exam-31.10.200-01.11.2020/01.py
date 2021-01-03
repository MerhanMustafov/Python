num_of_people = int(input())
nights = int(input())
transport_cards = int(input())
tickets = int(input())

totol_nights = 20 * nights
totol_cards = transport_cards * 1.6
total_tickets = tickets * 6
per_person = totol_nights + totol_cards + total_tickets
whole_group = per_person * num_of_people * 1.25
print(f'{whole_group:.2f}')