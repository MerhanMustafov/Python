price_flour_per_kg = float(input())

flour_kg = float(input())
shugar_kg = float(input())
number_eggs_barks = int(input())
yeast_package = int(input()) # Yeast - Мая

price_shugar = price_flour_per_kg * 0.75
price_eggs = price_flour_per_kg * 1.1
price_yeast = price_shugar * 0.2

total_sum_flour = flour_kg * price_flour_per_kg
total_sum_shugar = shugar_kg * price_shugar
total_sum_eggs = number_eggs_barks * price_eggs
total_sum_yeast = yeast_package * price_yeast

total = total_sum_flour + total_sum_shugar + total_sum_eggs + total_sum_yeast
print(f'{total:.2f}')
