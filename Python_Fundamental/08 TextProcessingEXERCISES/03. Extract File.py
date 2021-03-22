path_to_file = input()
point_index = path_to_file.index(".")
ind = 0
for l in range(len(path_to_file)-1,-1,-1):
    if path_to_file[l] == '\\':
        ind = l
        break
file_name = "".join(list(reversed(path_to_file[point_index-1:ind:-1])))
file_extension = "".join(list(reversed(path_to_file[:point_index:-1])))
print(f"File name: {file_name}")
print(f"File extension: {file_extension}")

# https://pastebin.com/7Ab65Y5m

# directory = input().split("\\")
# file_name, extension = directory[-1].split(".")
#
# print(f"File name: {file_name}")
# print(f"File extension: {extension}")

# https://pastebin.com/ZJwTiVQi