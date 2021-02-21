population = input().split(", ")
minimum_welth = int(input())

for one in range(len(population)):
    population = [int(i) for i in population ]
    m = max(population)
    ind = population.index(m)
    if int(population[one]) < minimum_welth:
        m -= (minimum_welth - int(population[one]))
        population[ind] = m
        population[one] = minimum_welth
if any(y < minimum_welth for y in population):

    print("No equal distribution possible")
else:
    print(population)
