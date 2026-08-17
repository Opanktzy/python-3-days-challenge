

products = {
    "laptop": 7000000,
    "mouse": 150000,
    "keyboard": 300000,
    "monitor": 2000000
}
def main():
    print("=" * 50)
    print("1. Lihat Produk")
    print("2. Cari Produk")
    print("3. Tambah Produk")
    print("4. Update Harga")
    print("5. Hapus Produk")
    print("6. Hitung Total Harga Semua Produk")
    print("7. Keluar")
    choice = input("Pilih Menu: ")
    if choice == "1":
        look_up_product()
    elif choice == "2":
        look_for_product()
    elif choice == "3":
        add_product()
    elif choice == "4":
        update_product()
    elif choice == "5":
        delete_product()
    elif choice == "6":
        calculate_total_price()
    elif choice == "7":
        print("Terima kasih!")
    else:
        print("Pilihan tidak valid.")

def look_up_product():
    lookup = input("Masukan nama produk: ")
    if lookup in products:
        print(f"Harga {lookup}: {products[lookup]}")
    else:
        print("Produk tidak ditemukan.")
        return main()
def look_for_product():
    lookup = input("Masukan Nama Produk: ")
    if lookup in products:
        print(f"Produk {lookup} ditemukan.")
    else:
        print("Produk tidak ditemukan.")
def add_product():
    name = input("Masukan Nama Produk : ")
    price = int(input("Masukan Harga Produk: "))
    products[name] = price
    print(f"Produk {name} berhasil ditambahkan.")
    return main()
def update_product():
    name = input("Masukan Nama Produk: ")
    if name in products:
        price = int(input("Masukan Harga: "))
        products[name] = price
        print(f"Produk {name} berhasil diperbarui.")
        return main()
    else:
        print("Produk tidak ditemukan.")
        return main()
def delete_product():
    name = input("Masukan Nama Produk: ")
    if name in products:
        del products[name]
        print(f"Produk {name} berhasil dihapus.")
        return main()
    else:
        print("Produk tidak ditemukan.")
        return main()
def calculate_total_price():
    total = sum(products.values())
    print(f"Total harga semua produk: {total}")
    return main()


main()
