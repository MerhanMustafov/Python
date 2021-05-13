def callecting_usernames(n):
    all_usernames = []
    for username in range(n):
        all_usernames.append(input())
    return all_usernames


n = int(input())
all_usernames = callecting_usernames(n)
all_usernames = set(all_usernames)
for u in all_usernames:
    print(u)

# n = int(input())
# all_usernames = []
# for username in range(n):
#     all_usernames.append(input())
# all_usernames = set(all_usernames)
# for u in all_usernames:
#     print(u)