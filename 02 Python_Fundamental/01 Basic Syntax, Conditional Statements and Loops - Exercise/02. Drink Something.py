age = int(input())

kids = 'toddy'
teens = 'coke'
young_adults = 'beer'
adults = 'whisky'

if age <= 14:
    print(f'drink {kids}')
elif age <= 18:
    print(f'drink {teens}')
elif age <= 21:
    print(f'drink {young_adults}')
elif age > 21:
    print(f'drink {adults}')