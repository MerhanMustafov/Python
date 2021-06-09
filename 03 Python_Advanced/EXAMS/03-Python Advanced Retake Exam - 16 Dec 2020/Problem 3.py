def get_magic_triangle(n):
    triangle = []
    while not len(triangle) == n:
        if not triangle:
            triangle.append([1])
        elif len(triangle) == 1:
            triangle.append([1, 1])
        else:
            triangle_part = []
            for x in range(len(triangle[-1])):
                if x == 0:
                    triangle_part.append(1)

                elif x == len(triangle[-1])-1:
                    num = triangle[-1][x - 1] + triangle[-1][x]
                    triangle_part.append(num), triangle_part.append(1)

                else:
                    b = triangle[-1][x - 1] + triangle[-1][x]
                    triangle_part.append(b)
            triangle.append(triangle_part)

    return triangle

# n = int(input())
# print(get_magic_triangle(n))