import math
figure = str(input())
if figure == 'square':
    a = float(input())
    print(f'{a*a:.3f}')
elif figure == 'rectangle':
    a = float(input())
    b = float(input())
    print(f'{a*b:.3f}')
elif figure == 'circle':
    from math import  pi
    a = float(input())
    r = a * a * pi
    print(f'{r:.3f}')
elif figure == 'triangle':
    a = float(input())
    b = float(input())
    reesult = (a * b) / 2
    print(f'{reesult:.3f}')
