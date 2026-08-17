data = [10, 20, 30, 40, 50]
def linear_search(data, target):
    if target in data:
        print(f"Angka {target} ditemukan.")
        print(f"Angka Ditemukan pada indeks {data.index(target)}")
    else:
        print(f"Angka {target} tidak ditemukan.")

linear_search(data, 20)
