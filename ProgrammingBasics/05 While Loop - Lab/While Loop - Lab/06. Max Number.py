import sys
comand = input()
max = -sys.maxsize

while comand != "Stop":
    number = int(comand)
    if number > max:
        max = number
    comand = input()
else:
    print(max)