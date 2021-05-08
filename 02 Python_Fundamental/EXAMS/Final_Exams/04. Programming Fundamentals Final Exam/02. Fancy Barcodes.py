import re
n = int(input())
pattern = r"(@)#+[A-Z][A-Za-z0-9]{4,}[A-Z]\1#+"
for _ in range(n):
    barcode = input()
    if re.match(pattern, barcode):
        barcode = list(barcode)
        product_group = [x for x in barcode if x.isdigit()]
        if product_group:
            print(f"Product group: {''.join(product_group)}")
        else:
            print(f"Product group: 00")
    else:
        print("Invalid barcode")