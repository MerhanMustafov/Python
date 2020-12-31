degree = float(input())
if degree >= 26.00 and degree <= 35.00:
    print("Hot")
elif degree >= 20.1 and degree <= 25.9:
    print("Warm")
elif degree >= 15.00 and degree <=20.00:
    print("Mild")
elif degree >= 12.00 and degree <=14.9:
    print("Cool")
elif degree >=5.00 and degree <=11.9:
    print("Cold")
else:
   print("unknown")
