# •	На първия ред - минути разходка на ден - цяло число в интервала [1...50]
# •	На втория ред - броят на разходките дневно - цяло число в интервала [1…10]
# •	На третия ред - приетите от котката калории на ден – цяло число в интервала [100…4000]
minutes = int(input())
number = int(input())
calorie = int(input())

total_minutes_walk = minutes * number
burned_calorie = total_minutes_walk * 5
calorie_percentage = calorie * 0.5
if burned_calorie >= calorie_percentage:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {burned_calorie}." )
elif burned_calorie < calorie_percentage:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {burned_calorie}.")



