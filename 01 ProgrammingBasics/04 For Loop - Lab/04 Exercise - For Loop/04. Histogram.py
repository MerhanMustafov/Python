n = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
for numbers in range (1, n +1):
    new_number = int(input())
    if new_number < 200:
        p1 += 1
    if 200 <= new_number <= 399:
        p2 +=1
    if 400 <= new_number <= 599:
        p3 += 1
    if 600 <= new_number <= 799:
        p4 += 1
    if new_number >= 800:
        p5 += 1
print(f'{p1 / n * 100:.2f}%')
print(f'{p2 / n * 100:.2f}%')
print(f'{p3 / n * 100:.2f}%')
print(f'{p4 / n * 100:.2f}%')
print(f'{p5 / n * 100:.2f}%')

