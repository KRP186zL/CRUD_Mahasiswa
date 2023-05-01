bulan = int(input(">"))

def validasi(bulan):
    if bulan in [int(x) for x in range(10)]:
        new_bulan = str(bulan).replace(str(bulan),f"0{bulan}")
        return new_bulan

print(validasi(bulan))