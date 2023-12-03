import  re
n= int(input())

pattern =r'@#+([A-Z][a-zA-Z0-9]{4,}[A-Z])@#+'
barcodes_list = []
for _ in range(n):
    barcode = input()
    match = re.fullmatch(pattern,barcode)
    if match:
        group = re.findall(r"\d",barcode)
        if group:
            print(f'Product group: {"".join(group)}')
        else:
            print(f'Product group: 00')

    else:
        print(f"Invalid barcode")