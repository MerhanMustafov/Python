# •	Брой отворени табове в браузъра n - цяло число в интервала [1...10]
# •	Заплата - число в интервала [700...1500]
tab = int(input())
salary = int(input())
remain_salary = 0

for tabS in range (1, tab + 1):
    text = input()
    if text == 'Facebook':
       salary -= 150
    elif text == 'Instagram':
       salary -= 100
    elif text == 'Reddit':
        salary -= 50
    else:
        salary = salary
    if salary <= 0:
        print("You have lost your salary.")
        break
if salary > 0:
    print(salary)