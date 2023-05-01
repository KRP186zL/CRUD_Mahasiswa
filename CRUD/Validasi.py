def validasi_date(tanggal:int,bulan:str,tahun:int)->any:
    if bulan > 12 or bulan < 1:
        return False
    if tahun < 1 or tahun >9999:
        return False
    if bulan in [4,6,9,11] and tanggal > 30:
        return False
    if bulan == 2:
        if (tahun % 4 == 0 and tahun % 100 != 0) or tahun % 400 == 0:
            return tanggal <= 29
        else: 
            return tanggal <= 28
    
    return tanggal <=31
