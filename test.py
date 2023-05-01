data = {
    "nama":" "*100
}


nama1 = data.copy

nama = input("masukkan nama: ")
sisa = len(data["nama"])-len(nama)

data["nama"] = nama + "k"*sisa

print(data["nama"])
print(len(data["nama"]))


from .import Template_data,database,Validasi


def data_pertama():


    data = Template_data.TEMPLATE.copy()
    nama = input("Masukkan nama mahasiswa: ")
    while True:
        try:
            tahun = int(input("Masukkan Tahun(4 digit)\t: "))
            bulan = int(input("Masukkan Bulan(1-12)\t: "))
            tanggal = int(input("Masukkan Tanggal(1-31)\t: "))
            if Validasi.validasi_date(tanggal,bulan,tahun):
                break
            else:
                print("\n\nTangggal, bulan, atau tahun tidak Valid, Silahkan coba lagi!")
            break
        except ValueError:
            print("\n\nTangggal, bulan, atau tahun tidak Valid, Silahkan coba lagi!")
    kelas = input("Masukkan kelas: ")
    prodi = input("Masukkan prodi: ")

    #Menghitung sisa spasi untuk template data
    sisa_panjang_nama = len(Template_data.TEMPLATE["nama"])-len(nama)
    sisa_panjang_kelas = len(Template_data.TEMPLATE["kelas"])-len(kelas)
    sisa_panjang_prodi = len(Template_data.TEMPLATE["prodi"])-len(prodi)

    data["nama"] = nama +" "*sisa_panjang_nama
    data["lahir"] = tanggal, "-", bulan, "-", tahun
    data["kelas"] = kelas +" "*sisa_panjang_kelas
    data["prodi"]= prodi +" "*sisa_panjang_prodi
    if True:
        data["pk"]+=1
    data_mahasiswa = f'{data["pk"]},{data["nama"]},{data["lahir"]},{data["kelas"]},{data["prodi"]}'

    try:
        with open(database.DB_NAME,"w",encoding="utf-8") as file :
            file.write(data_mahasiswa)
    except:
        print("Gagal !")


    