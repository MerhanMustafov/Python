def closest_num(x1, y1, x2, y2, x3, y3, x4, y4):
    first = abs(x2 - x1)+ abs(y2 - y1)
    second = abs(x4 - x3) + abs(y4 - y3)

    if first >= second:
        is_first_closer = closer_one(x1, y1, x2, y2)
        if is_first_closer:
            return (f"({int(x1)}, {int(y1)})({int(x2)}, {int(y2)})")
        else:
            return (f"({int(x2)}, {int(y2)})({int(x1)}, {int(y1)})")

    else:
        is_first_closer = closer_one(x3, y3, x4, y4)
        if is_first_closer:
            return (f"({int(x3)}, {int(y3)})({int(x4)}, {int(y4)})")
        else:
            return (f"({int(x4)}, {int(y4)})({int(x3)}, {int(y3)})")

def closer_one(x1, y1, x2, y2):
    first = abs(x1 * x1 + y1 * y1)
    second = abs(x2 * x2 + y2 * y2)
    is_first_closer = True

    if first <= second:
        is_first_closer = True
    else:
        is_first_closer = False
    return is_first_closer


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())

result = closest_num(x1, y1, x2, y2, x3, y3, x4, y4)
print(result)


