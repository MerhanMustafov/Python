the_event = input()
numbers_coffee = 0

while the_event != "END":
    if the_event == "coding" or the_event == "dog" or the_event == "cat" or the_event == "movie":
        numbers_coffee += 1
    elif the_event.upper() == "CODING" or the_event.upper() == "DOG" or the_event.upper() == "CAT" \
        or the_event.upper() == "MOVIE":
        numbers_coffee += 2
    the_event = input()

if numbers_coffee <= 5:
    print(numbers_coffee)
else:
    print("You need extra sleep")