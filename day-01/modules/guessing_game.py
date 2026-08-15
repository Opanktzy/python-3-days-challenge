import random as r
print("="*20)
print("Selamat datang di permainan tebak angka!")
print("Komputer Telah Memilih Angka Acak antara 1 sampai 50.")
print("Kamu memiliki 5 kesempatan untuk menebak angka.")
print("="*20)

#1. Generate angka acak
angka_rahasia = r.randint(1, 50)
kesempatan = 5

#2. Loop untuk menebak angka
while kesempatan > 0:
    try:
        tebakan = int(input("Masukan Tebakan Anda : "))
        if tebakan == angka_rahasia:
            print("Selamat! Anda berhasil menebak angka.")
            break
        elif tebakan > angka_rahasia:
            print("Tebakan Anda terlalu tinggi.")
        elif tebakan < angka_rahasia:
            print("Tebakan Anda terlalu rendah.")
        else:
            print("Tebakan Anda salah.")
        kesempatan -= 1
        print("-"*30)
    except ValueError:
        print("Masukan harus berupa angka.")

if kesempatan == 0:
    print(f"\n👻 Game Over! Kamu kehabisan kesempatan. Angka yang benar adalah {angka_rahasia}.")
