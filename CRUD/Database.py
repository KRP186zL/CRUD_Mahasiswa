#Mengecek Database

DB_NAME = "Database../data.txt"

def cek_database():
    try:
        with open(DB_NAME,"r")  as file :
            print("Database tersedia")
    except:
        with open(DB_NAME,"w",encoding="utf-8") as file :
            print("Database tidak tersedia, membuat database baru")
