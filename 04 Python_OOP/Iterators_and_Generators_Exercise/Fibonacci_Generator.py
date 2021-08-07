def fibonacci():
    # a, b = 0, 1
    previous_number, current_num = 0, 1
    while True:
        yield previous_number
        previous_number, current_num = current_num, previous_number+current_num
        # yield a
        # b = a + b
        # a = b - a
generator = fibonacci()
for i in range(5):
    print(next(generator))
