class Example:
    text = 'Hello'

    def print_text(self):
        return 'SoftUni'

print(Example.text)	     # attribute reference
print(Example.print_text)  # attribute reference
x = Example()
print(x.print_text())	