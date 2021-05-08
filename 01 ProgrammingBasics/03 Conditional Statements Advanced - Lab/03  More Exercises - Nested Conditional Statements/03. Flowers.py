num_chrysanthemums = int(input())
num_roses = int(input())
num_tulips = int(input())
season = input()
holiday_Y_or_N = input()

price_chrysanthemums = 0
price_roses = 0
price_tulips = 0
whole_bucket_price = 0
whole_flowers_number = num_chrysanthemums + num_roses + num_tulips

engage_sum = 2

if season == "Spring":
    price_chrysanthemums = 2
    price_roses = 4.1
    price_tulips = 2.5
    whole_bucket_price = (price_chrysanthemums * num_chrysanthemums) + (price_roses * num_roses) + (price_tulips * num_tulips)

    if 7 < num_tulips:
        whole_bucket_price = whole_bucket_price * 0.95

elif season == "Summer":
    price_chrysanthemums = 2
    price_roses = 4.1
    price_tulips = 2.5
    whole_bucket_price = (price_chrysanthemums * num_chrysanthemums) + (price_roses * num_roses) + (price_tulips * num_tulips)

elif season == "Autumn":
    price_chrysanthemums = 3.75
    price_roses = 4.5
    price_tulips = 4.15
    whole_bucket_price = (price_chrysanthemums * num_chrysanthemums) + (price_roses * num_roses) + (price_tulips * num_tulips)

elif season == "Winter":
    price_chrysanthemums = 3.75
    price_roses = 4.5
    price_tulips = 4.15
    whole_bucket_price = (price_chrysanthemums * num_chrysanthemums) + (price_roses * num_roses) + (price_tulips * num_tulips)
    if 10 <= num_roses:
        whole_bucket_price = whole_bucket_price * 0.9

if whole_flowers_number > 20:
    whole_bucket_price *= 0.80
if holiday_Y_or_N == "Y":
    whole_bucket_price = whole_bucket_price * 1.15
elif holiday_Y_or_N == "N":
    whole_bucket_price = whole_bucket_price


print(f"{whole_bucket_price + engage_sum:.2f}")


