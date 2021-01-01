import sys
comand = input()
min = sys.maxsize

while comand != "Stop":
    number = int(comand)
    if number < min:
        min = number
    comand = input()
else:
    print(min)