group_number = int(input())
musala = 0
monblan = 0
kilimanjaro = 0
k2 = 0
everest = 0
total_people = 0

for number in range(1, group_number + 1):
    number_of_people = int(input())
    total_people += number_of_people
    if number_of_people <= 5:
        musala += number_of_people
    elif 6 <= number_of_people <= 12:
        monblan += number_of_people
    elif 13 <= number_of_people <= 25:
        kilimanjaro += number_of_people
    elif 26 <= number_of_people <= 40:
        k2 += number_of_people
    elif number_of_people >= 41:
        everest += number_of_people
print(f'{musala/total_people*100:.2f}%')
print(f'{monblan/total_people*100:.2f}%')
print(f'{kilimanjaro/total_people*100:.2f}%')
print(f'{k2/total_people*100:.2f}%')
print(f'{everest/total_people*100:.2f}%')


