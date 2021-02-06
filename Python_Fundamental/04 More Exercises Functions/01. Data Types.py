def data_type_process(type, input):

    if type == "int":
        input = int(input)
        return input * 2
    elif type == "real":
        input = float(input)
        return (f"{input * 1.5:.2f}")
    elif type == "string":
        return (f'${input}$')



type = input()
input = input()
result = data_type_process(type, input)
print(result)
