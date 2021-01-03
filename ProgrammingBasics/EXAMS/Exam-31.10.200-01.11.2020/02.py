price_shirt = float(input())
needed_sum = float(input())
price_shorts = price_shirt * 0.75
price_socks = price_shorts * 0.20
price_boots = (price_shirt + price_shorts) * 2
total_sum = price_shirt + price_shorts + price_socks + price_boots
with_discount = total_sum * 0.85
if with_discount >= needed_sum:
    print("Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {with_discount:.2f} lv.")
else:
    print("No, he will not earn the world-cup replica ball.")
    print(f"He needs {abs(needed_sum - with_discount):.2f} lv. more.")