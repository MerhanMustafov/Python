lines = int(input())
up_to_now = 0
for times in range(lines):
    litres = int(input())
    if litres > 255:
        print(f"Insufficient capacity!")
        continue
    elif litres <= 255:
        if  up_to_now + litres > 255:
            print(f"Insufficient capacity!")
            continue
        up_to_now += litres
print(up_to_now)