current_hour = int(input())
current_minute = int(input()) + 15
if current_minute > 59:
    current_hour += 1
    current_minute -=60
if current_hour > 23:
    current_hour = 0
if current_minute < 10:
    current_minute = (f"0{current_minute}")
print(f'{current_hour}:{current_minute}')