import math as m

def main():
    while True:
        print("=== KALKULATOR ===")
        print("1. Pangkat")
        print("2. Akar Kuadrat")
        print("3. Pembulatan ke atas")
        print("4. Pembulatan ke bawah")
        print("5. Faktorial")
        print("6. Keluar")
        try:
            choice = int(input("Masukan Pilihan: "))
        except ValueError:
            print("Input Tidak Valid")
            continue
        if choice == 1:
            pangkat()
        elif choice == 2:
            akar_kuadrat()
        elif choice == 3:
            pembulatan_atas()
        elif choice == 4:
            pembulatan_bawah()
        elif choice == 5:
            faktorial()
        elif choice == 6:
            print("Terima Kasih")
            break
        else:
            print("Pilihan Tidak Valid")



def pangkat():
    try:
        num1 = int(input("Masukan Angka: "))
        pow = int(input("Masukan Angka Pangkat: "))
        print("")
    except ValueError:
        print("Input Tidak Valid")
        return
    result = m.pow(num1, pow)
    print(f"Hasil Dari : {num1}^{pow} = {result}")

def akar_kuadrat():
    try:
        num1 = int(input("Masukan Angka: "))
        print("")
    except ValueError:
        print("Input Tidak Valid")
        return
    result = m.sqrt(num1)
    print(f"Hasil Dari : √{num1} = {result}")

def pembulatan_atas():
    try:
        num1 = int(input("Masukan Angka: "))
        print("")
    except ValueError:
        print("Input Tidak Valid")
        return
    result = m.ceil(num1)
    print(f"Hasil Dari : Pembulatan ke atas {num1} = {result}")

def pembulatan_bawah():
    try:
        num1 = int(input("Masukan Angka: "))
        print("")
    except ValueError:
        print("Input Tidak Valid")
        return
    result = m.floor(num1)
    print(f"Hasil Dari : Pembulatan Bawah {num1} = {result}")

def faktorial():
    try:
        num1 = int(input("Masukan Angka: "))
        print("")
    except ValueError:
        print("Input Tidak Valid")
        return
    result = m.factorial(num1)
    print(f"Hasil Dari : Faktorial {num1} = {result}")

main()
