degree = float(input())
if degree >= 26.00:
    if degree <= 35.00:
        print("Hot")

if degree >= 20.1:
    if degree <= 25.9:
        print("Warm")

if degree >= 15.00:
    if degree <= 20.00:
        print("Mild")

if degree >= 12.00:
    if degree <= 14.9:
        print("Cool")

if degree >= 5.00:
    if degree <= 11.9:
        print("Cold")

if degree <= 4.9:
    print("unknown")
if degree >= 35.1:
    print("unknown")