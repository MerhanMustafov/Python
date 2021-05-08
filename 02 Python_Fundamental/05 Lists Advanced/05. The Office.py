happines = [int(el) for el in input().split()]
factor = int(input())
multiplied_hapinnes_by_factor = [num*factor for num in happines]
# multiplied_hapinnes_by_factor = list(map(lambda num: num*factor, happines))
avg_happines = sum(multiplied_hapinnes_by_factor) / len(multiplied_hapinnes_by_factor)



happy_employees = [h for h in multiplied_hapinnes_by_factor if h > avg_happines]

# happy_employees = []
# for h in multiplied_hapinnes_by_factor:
#     if h >=avg_happines:
#         happy_employees.append(h)

# happy_employees = list(filter(lambda h: h > avg_happines, multiplied_hapinnes_by_factor))

half_n = len(multiplied_hapinnes_by_factor) / 2

if len(happy_employees) >= half_n:
    print(f"Score: {len(happy_employees)}/{len(multiplied_hapinnes_by_factor)}. Employees are happy!")
else:
    print(f"Score: {len(happy_employees)}/{len(multiplied_hapinnes_by_factor)}. Employees are not happy!")