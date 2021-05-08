command = input()
total_without_taxes = 0
while not command == "special" and not command == "regular":
    vluee = float(command)
    if vluee < 0:
        print(f"Invalid price!")
        command = input()
        continue
    total_without_taxes += vluee
    command = input()
if total_without_taxes > 0:
    final_price = total_without_taxes * 1.2
    if command == "special":
        final_price *= 0.9
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_without_taxes:.2f}$")
    print(f"Taxes: {total_without_taxes * 0.2:.2f}$")
    print("-----------")
    print(f"Total price: {final_price:.2f}$")
else:
    print(f"Invalid order!")