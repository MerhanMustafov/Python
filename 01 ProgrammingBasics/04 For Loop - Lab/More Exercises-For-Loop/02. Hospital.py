period = int(input())
doctors = 7
treated = 0
untreated = 0

for day in range(1, period+1):
    if day % 3 == 0:
        if untreated > treated:
            doctors += 1
    number_patients_for_a_day = int(input())
    if number_patients_for_a_day <= doctors:
        treated += number_patients_for_a_day

    elif number_patients_for_a_day > doctors:
        treated += doctors
        untreated += number_patients_for_a_day - doctors

print(f"Treated patients: {treated}.")
print(f"Untreated patients: {untreated}.")
