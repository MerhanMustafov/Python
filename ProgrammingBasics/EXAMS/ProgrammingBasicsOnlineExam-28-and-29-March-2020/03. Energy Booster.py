fruit = input()
size = input()
number_sets = int(input())
price_small_or_big = 0


if fruit == "Watermelon":
    if size == "small":
        price_small_or_big = 56 * 2
    elif size == "big":
        price_small_or_big = 28.7 * 5
elif fruit == "Mango":
    if size == "small":
        price_small_or_big = 36.66 * 2
    elif size == "big":
        price_small_or_big = 19.6 * 5
elif fruit == "Pineapple":
    if size == "small":
        price_small_or_big = 42.1 * 2
    elif size == "big":
        price_small_or_big = 24.8 * 5
elif fruit == "Raspberry":
    if size == "small":
        price_small_or_big = 20 * 2
    elif size == "big":
        price_small_or_big = 15.2 * 5

price_sets = price_small_or_big * number_sets

if 400 <= price_sets <= 1000:
    price_sets *= 0.85
elif 1000 < price_sets:
    price_sets *= 0.50
print(f"{price_sets:.2f} lv.")
