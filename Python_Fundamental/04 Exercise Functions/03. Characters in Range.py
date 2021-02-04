
def symbols_inbetween(symbol_one, symbol_two):
    result = ""
    for symbol in range(ord(symbol_one) + 1, ord(symbol_two)):
        result += chr(symbol) + " "
    return result

symbol_one = input()
symbol_two = input()
print(symbols_inbetween(symbol_one, symbol_two))