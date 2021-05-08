# string = input()
# for p in range(len(string)):
#     if string[p] == ":":
#         print(f"{string[p]}{string[p+1]}")

# https://pastebin.com/5NgQhiTn

text = input()
emoji = [f'{text[index]}{text[index+1]}' for index in range(0, len(text)) if text[index] == ":"]
print("\n".join(emoji))