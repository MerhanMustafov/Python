w = float(input())
h = float(input())

koridor = 1
w_rab_mqsto = 1.2
h_rab_mqsto = 0.7

h1 = (h - koridor) / h_rab_mqsto
import math

h2 = math.floor(h1)

w1 = w / w_rab_mqsto
w2 = math.floor(w1)

result = w2 * h2 - 3
print(result)
