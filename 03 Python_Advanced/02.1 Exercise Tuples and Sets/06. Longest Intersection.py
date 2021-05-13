

n = int(input())
intersections = []
for _ in range(n):
    data = input()
    first_seq_data, second_seq_ddata = data.split("-")
    start, stop = [int(el) for el in first_seq_data.split(",")]
    first_seq = range(start, stop+1)
    start, stop = [int(el) for el in second_seq_ddata.split(",")]
    sec_seq = range(start, stop+1)
    intersection = set(first_seq).intersection(sec_seq)
    intersections.append(intersection)
longest = sorted(intersections, key=lambda x: -len(x))[0]
# print(f"Longest intersection is {list(longest)} with length {len(longest)}")
print(f"Longest intersection is [{', '.join([str(el) for el in longest])}] with length {len(longest)}")
