def strs_to_ints(strs):
    return [int(x) for x in strs]
def read_matrix(n):
    return [strs_to_ints(input().split(", ")) for _ in range(n)]
n = int(input())
matrix = read_matrix(n)
print([x for row in matrix for x in row])
