from . import Template_data,database

def data_pertama(nama:str,kelas:str,prodi:str,*args)->any:

    data = Template_data.TEMPLATE.copy()

    #tambahkan 0 jika bulan kurang dari 10
    if args[1] in[int(x) for x in range(10)]:
        new_bulan = str(args[1]).replace(str(args[1]),f"0{args[1]}")
        data["lahir"] = f"{args[0]}-{new_bulan}-{args[2]}"
    else:
        data["lahir"] = f"{args[0]}-{args[1]}-{args[2]}"


    #sesudah + berfungsi untuk mengambil sisa dari panjang input(nama,kelas,prodi)
    data["nama"] = nama + Template_data.TEMPLATE["nama"][len(nama):]
    data["kelas"] = kelas + Template_data.TEMPLATE["kelas"][len(kelas):]
    data["prodi"]= prodi + Template_data.TEMPLATE["prodi"][len(prodi):]

    data_mahasiswa = f'{data["pk"]+1},{data["lahir"]},{data["nama"]},{data["kelas"]},{data["prodi"]}'

    try:
        with open(database.DB_NAME,"w",encoding="utf-8") as file :
            file.write(data_mahasiswa,)
    except:
        print("Gagal !")


    