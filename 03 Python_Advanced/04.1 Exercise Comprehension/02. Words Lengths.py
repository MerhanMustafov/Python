text = input().split(", ")
final = [f"{x} -> {len(x)}" for x in text]
print(', '.join(final))