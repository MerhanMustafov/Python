def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        b = a + b
        a = b - a
generator = fibonacci()
for i in range(10):
    print(next(generator))
