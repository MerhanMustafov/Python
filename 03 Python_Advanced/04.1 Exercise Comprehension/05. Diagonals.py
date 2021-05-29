def str_to_int():
    return [int(x)for x in input().split(", ")]

def read_matrix(n):
    return [str_to_int() for line in range(n)]

def first_diagonal(matrix):
    diagonal = [matrix[num][num] for num in range(len(matrix))]
    sum_diagonal = sum(diagonal)
    return diagonal, sum_diagonal

def second_diagonal(matrix):
    diagonal = []
    count = -1
    for num in range(len(matrix)):
        diagonal.append(matrix[num][count])
        count -= 1
    sum_diagonal = sum(diagonal)
    return diagonal, sum_diagonal

matrix = read_matrix(int(input()))
print(f"First diagonal: {', '.join([str(num)for num in first_diagonal(matrix)[0]])}. Sum: {first_diagonal(matrix)[1]}")
print(f"Second diagonal: {', '.join([str(num)for num in second_diagonal(matrix)[0]])}. Sum: {second_diagonal(matrix)[1]}")