def main():
    while True:
        print("="*50)
        print("CALCULATOR")
        print("="*50)
        print("1. Tambah")
        print("2. Kurang")
        print("3. Kali")
        print("4. Bagi")
        print("5. Keluar")
        try:
            choice = input("Pilih operasi [1, 2, 3, 4, 5]: ")
            if choice == "5":
                break
            elif choice == "1":
                tambah()
            elif choice == "2":
                kurang()
            elif choice == "3":
                kali()
            elif choice == "4":
                bagi()
        except ValueError:
            print("Pilihan tidak valid. Silakan pilih antara 1, 2, 3, 4, atau 5.")

def tambah():
    try:
        a = float(input("Masukkan angka pertama: "))
        b = float(input("Masukkan angka kedua: "))
        print(f"Hasil: {a + b}")
        return
    except ValueError:
        print("Input tidak valid. Silakan masukkan angka.")

def kurang():
    try:
        a = float(input("Masukkan angka pertama: "))
        b = float(input("Masukkan angka kedua: "))
        print(f"Hasil: {a - b}")
        return
    except ValueError:
        print("Input tidak valid. Silakan masukkan angka.")

def kali():
    try:
        a = float(input("Masukkan angka pertama: "))
        b = float(input("Masukkan angka kedua: "))
        print(f"Hasil: {a * b}")
        return
    except ValueError:
        print("Input tidak valid. Silakan masukkan angka.")

def bagi():
    try:
        a = float(input("Masukkan angka pertama: "))
        b = float(input("Masukkan angka kedua: "))
        print(f"Hasil: {a / b}")
        return
    except ValueError:
        print("Input tidak valid. Silakan masukkan angka.")

main()
