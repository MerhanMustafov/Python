# Type of Fire	Range
# High	81 - 125
# Medium	51 - 80
# Low	1 - 50
RANGE_HIGH = range(81, 126)
RANGE_MEDIUM = range(51, 81)
RANGE_LOW = range(1, 51)

effort = 0

string = input().split("#")
water_amount = int(input())
# print(string)
put_out_fire= []


for fire in string:
    type_fire, value = fire.split(" = ")
    value = int(value)
    if type_fire == "High" and value not in  RANGE_HIGH:
        continue
    elif type_fire == "Medium" and value not in  RANGE_MEDIUM:
        continue
    elif type_fire == "Low" and value not in  RANGE_LOW:
        continue

    if water_amount >= value:
        water_amount -= value
        effort += value * 0.25
        put_out_fire.append(value)
print("Cells:")
for fire_value in put_out_fire:
    print(f" - {fire_value}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {sum(put_out_fire)}")

