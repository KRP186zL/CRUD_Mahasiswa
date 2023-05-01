from . import Operasi,Validasi

#Mengecek Database
DB_NAME = "Database/data.txt"

def cek_database():
    try:
        with open(DB_NAME,"r")  as file :
            print("Database tersedia")
    except:
        print("Database tidak tersedia, membuat database baru")
        with open(DB_NAME,"w",encoding="utf-8") as file :
            nama = input("Masukkan nama mahasiswa: ")
            while True:
                try:
                    while True:
                        tahun = int(input("Masukkan Tahun(4 digit)\t: "))
                        bulan = int(input("Masukkan Bulan(1-12)\t: "))
                        tanggal = int(input("Masukkan Tanggal(1-31)\t: "))
                        if Validasi.validasi_date(tanggal,bulan,tahun):
                            break
                        else: 
                            print("\n\nTangggal, bulan, atau tahun tidak Valid, Silahkan coba lagi!")
                            continue
                    break
                except ValueError:
                    print("\n\nTangggal, bulan, atau tahun tidak Valid, Silahkan coba lagi!")
            kelas = input("Masukkan kelas: ")
            prodi = input("Masukkan prodi: ")
            Operasi.data_pertama(nama,kelas,prodi,tanggal,bulan,tahun)

            