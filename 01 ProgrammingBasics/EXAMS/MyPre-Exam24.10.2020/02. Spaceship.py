# •	На първия ред е широчината на кораба - реално число в интервала [1.00... 10.00]
# •	На втория ред е  дължината на кораба - реално число в интервала [1.00…10.00]
# •	На третия ред е височината на кораба - реално число в интервала [1.00…20.00]
# •	На четвъртия ред е средната височина на астронавтите  -  реално число в интервала [1.50 … 1.90]
import math
ship_weigth = float(input())
ship_legth = float(input())
ship_higth = float(input())
average_heigth_astronavt = float(input())
volume_rocket = ship_weigth * ship_legth * ship_higth
volume_per_room = (average_heigth_astronavt + 0.4)*2*2
num_austronafts = math.floor(volume_rocket/volume_per_room)
if 3 <= num_austronafts <= 10:
    print(f"The spacecraft holds {num_austronafts} astronauts." )
elif num_austronafts < 3:
    print("The spacecraft is too small.")
elif num_austronafts > 10:
    print("The spacecraft is too big.")
