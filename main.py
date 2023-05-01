import os
import CRUD as CRUD
if __name__ == "__main__":
    sistem_operasi = os.name
    CRUD.database.cek_database()
    while True:
        match sistem_operasi:
            case "posix":os.system("clear") 
            case "nt":os.system("cls") 
        
        print(f"""{'='*100}
{'DATABASE MAHASISWA':^100}
{'='*100}
1. Tambah Mahasiswa
2. Lihat Mahasiswa
3. Update Mahasiswa
4. Delete Mahasiswa
5. Keluar
Silahkan Pilih""")
        pilih_menu = input("Pilih: ")
        match pilih_menu:
            case "1":pass
            case "2":pass
            case "3":pass
            case "4":pass
            case "5": exit()