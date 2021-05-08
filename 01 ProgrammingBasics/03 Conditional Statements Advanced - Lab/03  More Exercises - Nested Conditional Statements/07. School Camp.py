# 1.	Сезонът – текст - “Winter”, “Spring” или “Summer”;
# 2.	Видът на групата – текст - “boys”, “girls” или “mixed”;
# 3.	Брой на учениците – цяло число в интервала [1 … 10000];
# 4.	Брой на нощувките – цяло число в интервала [1 … 100].
season = input()
group_type = input()
number_of_student = int(input())
nights = int(input())
price = 0
sport = ""
if season == "Winter":
    if group_type == "boys":
        sport = "Judo"
        price = 9.60 * nights * number_of_student
    elif group_type == "girls":
        sport = "Gymnastics"
        price = 9.60 * nights * number_of_student
    elif group_type == "mixed":
        sport = "Ski"
        price = 10 * nights * number_of_student

elif season == "Spring":
    if group_type == "boys":
        sport = "Tennis"
        price = 7.20 * nights * number_of_student
    elif group_type == "girls":
        sport = "Athletics"
        price = 7.20 * nights * number_of_student
    elif group_type == "mixed":
        sport = "Cycling"
        price = 9.50 * nights * number_of_student

elif season == "Summer":
    if group_type == "boys":
        sport = "Football"
        price = 15 * nights * number_of_student
    elif group_type == "girls":
        sport = "Volleyball"
        price = 15 * nights * number_of_student
    elif group_type == "mixed":
        sport = "Swimming"
        price = 20 * nights * number_of_student


if number_of_student >= 50:
    price *= 0.5
elif 20 <= number_of_student < 50:
    price *= 0.85
elif 10 <= number_of_student < 20:
    price *= 0.95
print(f"{sport} {price:.2f} lv.")
