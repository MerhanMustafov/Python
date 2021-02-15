total_electrons = int(input())
shell = 1
result = []
while total_electrons > 0:
    if 2 * (shell ** 2) > total_electrons:
        result.append(total_electrons)
        break
    total_electrons -= 2 * (shell**2)
    result.append(2 * (shell**2))
    shell += 1
print(result)