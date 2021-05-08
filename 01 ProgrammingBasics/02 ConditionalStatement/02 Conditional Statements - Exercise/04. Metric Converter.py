number = float(input())
vxodna_merna_edinica = str(input())
izxodna_merna_edinica = str(input())
if vxodna_merna_edinica == "mm" and izxodna_merna_edinica == "cm":
    print(f'{(number / 10):.3f}')
if vxodna_merna_edinica == "mm" and izxodna_merna_edinica == "m":
    print(f'{(number / 1000):.3f}')
if vxodna_merna_edinica == "cm" and izxodna_merna_edinica == "mm":
    print(f'{(number * 10):.3f}')
if vxodna_merna_edinica == "cm" and izxodna_merna_edinica == "m":
    print(f'{(number / 100):.3f}')
if vxodna_merna_edinica == "m" and izxodna_merna_edinica == "cm":
    print(f'{(number * 100):.3f}')
if vxodna_merna_edinica == "m" and izxodna_merna_edinica == "mm":
   print(f'{(number*1000):.3f}')