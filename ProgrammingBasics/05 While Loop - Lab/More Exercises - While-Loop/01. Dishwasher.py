number_of_detergent = int(input())
detergent_ml = number_of_detergent * 750
day = 0
command = input()
number_plates = 0
number_saucepan = 0
while command != 'End':
    last = 0
    number_of_dishes = int(command)
    day += 1
    if day % 3 == 0:
        saucepan = number_of_dishes * 15
        number_saucepan += number_of_dishes
        last = saucepan
        if detergent_ml < saucepan:
            defference = abs(detergent_ml - last)
            print(f"Not enough detergent, {defference} ml. more necessary!")
            break
        detergent_ml -= saucepan
    else:
        plates = number_of_dishes * 5
        number_plates += number_of_dishes
        last = plates
        if detergent_ml < plates:
            defference = abs(detergent_ml - last)
            print(f"Not enough detergent, {defference} ml. more necessary!")
            break
        detergent_ml -= plates
    command = input()
if command == 'End':
    print("Detergent was enough!")
    print(f"{number_plates} dishes and {number_saucepan} pots were washed.")
    print(f"Leftover detergent {detergent_ml} ml.")
