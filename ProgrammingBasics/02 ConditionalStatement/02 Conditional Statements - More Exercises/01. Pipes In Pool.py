from math import fabs
v = int(input())
p1 = int(input())
p2=  int(input())
n = float(input())
p1*=n
p2*=n
totall_filled = p1 + p2
totall_filled_percentage = (totall_filled / v) * 100
p1_contribution = (p1 / totall_filled) * 100
p2_contribution = (p2 / totall_filled) * 100
if v >= totall_filled:
    print(f"The pool is {totall_filled_percentage}% full. Pipe 1: {(p1_contribution):.2f}%. Pipe 2: {(p2_contribution):.2f}%.")
elif v < totall_filled:
    print(f"For {n} hours the pool overflows with {fabs(v - totall_filled):.2f} liters.")

