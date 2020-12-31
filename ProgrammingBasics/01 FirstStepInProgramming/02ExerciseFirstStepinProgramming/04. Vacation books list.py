total_pages = int(input())
pages_per_hour = int(input())
days = int(input())
needs_time = total_pages / pages_per_hour
dayly_hours = needs_time / days
print(dayly_hours)