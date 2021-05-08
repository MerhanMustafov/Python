v = int(input())
p1 = int(input())
p2 = int(input())
n = float(input())

truba1 = p1 * n
truba2 = p2 * n
obshto_trubi = truba1 + truba2
obshto_trubi_procent = obshto_trubi / v * 100

prinos_truba1 = truba1 / obshto_trubi * 100
prinos_truba2 = truba2 / obshto_trubi * 100

if obshto_trubi < v:
    print(f"The pool is {obshto_trubi_procent}% full. Pipe 1: {prinos_truba1:.2f}%. Pipe 2: {prinos_truba2:.2f}.")



elif obshto_trubi > v:
    print(f"For {n} hours the pool overflows with {obshto_trubi - v:.2f} liters.")
