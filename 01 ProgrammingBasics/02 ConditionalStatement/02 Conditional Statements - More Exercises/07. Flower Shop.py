# •	Брой магнолии – цяло число в интервала [0 … 50]
# •	Брой зюмбюли – цяло число в интервала [0 … 50]
# •	Брой рози – цяло число в интервала [0 … 50]
# •	Брой кактуси – цяло число в интервала [0 … 50]
# •	Цена на подаръка – реално число в интервала [0.00 … 500.00]

from math import floor
from math import ceil
from math import fabs
magnolias = int(input()) * 3.25
zumbuls = int(input()) * 4
rouses =  int(input()) * 3.50
cactus = int(input()) * 8
preset_price = float(input())
totall_sum = (magnolias + zumbuls + rouses + cactus) * 0.95 #tax(0.05%)

if preset_price <= totall_sum:
    print(f'She is left with {floor(fabs(totall_sum - preset_price))} leva.')
elif preset_price > totall_sum:
    print(f'She will have to borrow {ceil(fabs(preset_price - totall_sum))} leva.')