deposite = float(input())
moths = int(input())
year_interest = float(input())

procent = deposite * year_interest / 100 / 12
sumata = deposite + moths * procent
print(sumata)


