age = float(input())
gender = str(input()) #m or f
if gender == 'f':
    if age >= 16:
        print('Ms.')
    elif age < 16:
        print('Miss')
elif gender == 'm':
    if age >= 16:
        print('Mr.')
    else:
        print("Master")
