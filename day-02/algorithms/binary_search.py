def binary_search(data, target):
    kiri = 0
    kanan = len(data) - 1

    while kiri <= kanan:
        mid = (kiri + kanan) // 2  # Mencari indeks tengah

        # Cek apakah target ada di tengah
        if data[mid] == target:
            return mid
        # Jika target lebih besar, abaikan bagian kiri
        elif data[mid] < target:
            kiri = mid + 1
        # Jika target lebih kecil, abaikan bagian kanan
        else:
            kanan = mid - 1

    return -1  # Data tidak ditemukan

# DATA WAJIB TERURUT
nilai = [4, 10, 16, 20, 30]
cari_angka = 30

hasil = binary_search(nilai, cari_angka)

if hasil != -1:
    print(f"Angka {cari_angka} ditemukan pada indeks ke-{hasil}")
else:
    print(f"Angka {cari_angka} tidak ditemukan.")
