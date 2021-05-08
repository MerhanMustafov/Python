command = input().split()
shortest = command[0]
longest = command[1]

if len(longest) < len(shortest):
    shortest = command[1]
    longest = command[0]
diff = abs(len(shortest) - len(longest))
total = 0
for current_pos in range(len(shortest)):
    total += ord(shortest[current_pos]) * ord(longest[current_pos])

if not diff == 0:
    longest = longest[-diff:]
    for el in range(len(longest)):
        total += ord(longest[el])
print(total)