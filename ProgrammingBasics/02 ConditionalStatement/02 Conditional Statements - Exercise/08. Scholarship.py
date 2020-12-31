from math import floor

income = float(input())
average_uspeh = float(input())
min_salary = float(input())
social_schoolarship = floor(min_salary * 0.35)
exellent_schoolarship = floor(average_uspeh * 25)

# if income < min_salary and average_uspeh > 4.50:
#     if average_uspeh >= 5.50 <= 6.00:
#         if exellent_schoolarship >= social_schoolarship:
#             print(f"You get a scholarship for excellent results {floor(exellent_schoolarship)} BGN")
#         elif exellent_schoolarship < social_schoolarship:
#             print(f"You get a Social scholarship {floor(social_schoolarship)} BGN")
#     else: или elif income < min_salary and average_uspeh > 4.50:
#         print(f"You get a Social scholarship {floor(social_schoolarship)} BGN")
# elif average_uspeh >= 5.50:
#     print(f"You get a scholarship for excellent results {floor(exellent_schoolarship)} BGN")
# else:
#     print("You cannot get a scholarship!")


if income < min_salary and average_uspeh >= 4.50 < 5.50:
    if average_uspeh >= 5.50 <= 6.00:
        if exellent_schoolarship >= social_schoolarship:
            print(f"You get a scholarship for excellent results {floor(exellent_schoolarship)} BGN")
        elif exellent_schoolarship <= social_schoolarship:
            print(f"You get a Social scholarship {floor(social_schoolarship)} BGN")
    elif income < min_salary and average_uspeh >= 4.50 < 5.50:
        print(f"You get a Social scholarship {floor(social_schoolarship)} BGN")

elif average_uspeh >= 5.50 <= 6.00:
    print(f"You get a scholarship for excellent results {floor(exellent_schoolarship)} BGN")
else:
    print("You cannot get a scholarship!")




