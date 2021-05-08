city = input()
sales = float(input())
percent = 0
if city == 'Sofia':
    if 0 <= sales <= 500:
        percent = 0.05
        print(f'{percent * sales:.2f}')
    elif 500 < sales <= 1000:
        percent = 0.07
        print(f'{percent * sales:.2f}')
    elif 1000 < sales <= 10000:
        percent = 0.08
        print(f'{percent * sales:.2f}')
    elif sales > 10000:
        percent = 0.12
        print(f'{percent * sales:.2f}')
    elif sales < 0:
        print('error')
elif city == 'Varna':
    if 0 <= sales <= 500:
        percent = 0.045
        print(f'{percent * sales:.2f}')
    elif 500 < sales <= 1000:
        percent = 0.075
        print(f'{percent * sales:.2f}')
    elif 1000 < sales <= 10000:
        percent = 0.1
        print(f'{percent * sales:.2f}')
    elif sales > 10000:
        percent = 0.13
        print(f'{percent * sales:.2f}')
    elif sales < 0:
        print('error')
elif city == 'Plovdiv':
    if 0 <= sales <= 500:
        percent = 0.055
        print(f'{percent * sales:.2f}')
    elif 500 < sales <= 1000:
        percent = 0.08
        print(f'{percent * sales:.2f}')
    elif 1000 < sales <= 10000:
        percent = 0.12
        print(f'{percent * sales:.2f}')
    elif sales > 10000:
        percent = 0.145
        print(f'{percent * sales:.2f}')
    elif  sales < 0:
        print('error')
else:
    print('error')

