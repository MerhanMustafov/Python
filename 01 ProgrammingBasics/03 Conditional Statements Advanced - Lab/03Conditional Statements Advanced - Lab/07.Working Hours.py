# час от денонощието(цяло число)
# ден от седмицата(текст)
# като работното време на офисът е от 10-18 часа, от понеделник до събота включително
twenty_four_hours = int(input())
day = input()
if 10 <= twenty_four_hours <= 18:
    if day == 'Monday':
        print('open')
    elif day == 'Tuesday':
        print('open')
    elif day == 'Wednesday':
        print('open')
    elif day == 'Thursday':
        print('open')
    elif day == 'Friday':
        print('open')
    elif day == 'Saturday':
        print('open')
    else:
        print('closed')
else:
    print('closed')
