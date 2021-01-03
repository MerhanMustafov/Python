easter_bread = int(input()) #Козунак  – 3.20 лв.
eggs_bark = int(input()) #кора с 12 яйца е 4,35
cookies_kg = int(input()) #Курабии – 5.40 лв. за килограм

# •	Боя за яйца - 0.15 лв. за яйце

price_easter_bread = easter_bread * 3.20
price_eggs_bark = eggs_bark * 4.35
price_cookies_kg = cookies_kg * 5.40
price_paint_for_eggs = eggs_bark * 12 * 0.15

total_price = price_easter_bread + price_eggs_bark + price_cookies_kg + price_paint_for_eggs

print(f'{total_price:.2f}')





