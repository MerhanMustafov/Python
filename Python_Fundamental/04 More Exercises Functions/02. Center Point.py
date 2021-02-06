def closest_num(x1, y1, x2, y2):
    if abs(x1) + abs(y1) < abs(x2) + abs(y2):
        return (f"({int(x1)}, {int(y1)})")
    else:
        return (f"({int(x2)}, {int(y2)})")


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
result = closest_num(x1,y1, x2, y2)
print(result)


