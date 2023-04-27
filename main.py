import os

if __name__ == "__main__":
    sistem_operasi = os.name

    while True:
        match sistem_operasi:
            case "posix":os.system("clear") 
            case "nt":os.system("cls") 
        
